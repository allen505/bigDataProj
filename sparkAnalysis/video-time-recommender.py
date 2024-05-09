from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, from_json
from pyspark.sql.types import StructType, StringType
from pymongo import MongoClient

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("KafkaToMongoDB") \
    .getOrCreate()

# Define the Kafka parameters
kafka_bootstrap_servers = "localhost:9093"
kafka_topic = "your_kafka_topic"

# Define the MongoDB connection parameters
mongo_uri = "mongodb://localhost:27017/"
database_name = "bigdata"
collection_name = "your_collection"

# Define the schema for the Kafka message
schema = StructType().add("video_id", StringType()).add("timestamp", StringType())

# Read data from Kafka into a Spark DataFrame
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic) \
    .load()

# Parse the value column as JSON
df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json("value", schema).alias("data")) \
    .select("data.*")

# Group by video_id and compute the average timestamp
avg_timestamp_df = df.groupBy("video_id").agg(avg("timestamp").alias("average_timestamp"))

# Convert video_id to string type for writing to MongoDB
avg_timestamp_df = avg_timestamp_df.withColumn("video_id", avg_timestamp_df["video_id"].cast(StringType()))

# Write the results to MongoDB
avg_timestamp_df.writeStream \
    .foreachBatch(lambda batch_df, batch_id: batch_df.write \
                  .format("com.mongodb.spark.sql.DefaultSource") \
                  .mode("append") \
                  .option("uri", mongo_uri + database_name + "." + collection_name) \
                  .save())

# Start the streaming query
query = avg_timestamp_df.writeStream \
    .outputMode("update") \
    .start()

# Wait for the streaming query to terminate
query.awaitTermination()

# Stop the SparkSession
spark.stop()

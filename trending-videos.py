from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window
from pyspark.sql.types import StringType
from pymongo import MongoClient

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("KafkaTrendingVideos") \
    .getOrCreate()

# Define Kafka parameters
kafka_params = {
    "kafka.bootstrap.servers": "localhost:9093",
    "subscribe": "video_watch_topic",
    "startingOffsets": "earliest"
}

# Define schema for the JSON data
schema = "user_id STRING, video_id STRING, watched_at TIMESTAMP"

# Read data from Kafka
raw_data = spark \
    .readStream \
    .format("kafka") \
    .options(**kafka_params) \
    .load()

# Parse JSON data
parsed_data = raw_data \
    .select(from_json(col("value").cast("string"), schema).alias("data")) \
    .select("data.*")

# Group by date and video_id to count occurrences
trending_videos = parsed_data \
    .groupBy(window(col("watched_at"), "1 day"), "video_id") \
    .count() \
    .orderBy(col("window"), col("count").desc())

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["bigdata"]
collection = db["trending_videos"]

# Define a function to write top 10 videos to MongoDB
def write_to_mongo(rows):
    top_videos = [row.video_id for row in rows[:10]]  # Extract only the top 10 videos
    collection.insert_one({"top_videos": top_videos})

# Start streaming query to continuously update the results
query = trending_videos \
    .writeStream \
    .outputMode("complete") \
    .foreachBatch(write_to_mongo) \
    .start()

# Await termination
query.awaitTermination()

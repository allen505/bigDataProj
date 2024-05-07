from json import loads
from kafka import KafkaConsumer

TOPIC_NAME = 'vidRecommender'
CONSUMER_GRP = 'my-group'

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id=CONSUMER_GRP,
    value_deserializer=lambda x: loads(x.decode('utf-8')))

TOPIC_NAME = 'vidRecommender'

print('Connected to Kafka')

for message in consumer:
    message = message.value
    print('Received value: {}'.format(message))

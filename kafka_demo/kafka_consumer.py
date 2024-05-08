from json import loads
from kafka import KafkaConsumer

TOPIC_NAME = 'test-topic'
CONSUMER_GRP = 'my-group'
PORT = '9093'

consumer = KafkaConsumer(
    TOPIC_NAME,
    # bootstrap_servers=['localhost:9092'],
    bootstrap_servers=['localhost:9093'],
    group_id=CONSUMER_GRP,
    value_deserializer=lambda x: loads(x.decode('utf-8'))
    )

print('Connected to Kafka')

while True:
    for message in consumer:
        message = message.value
        print('Received value: {}'.format(message))

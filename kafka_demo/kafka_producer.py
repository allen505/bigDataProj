from time import sleep
import json
from kafka import KafkaProducer
from kafka.errors import KafkaError
import logging

logger = logging.getLogger('kafka')
logger.setLevel(logging.DEBUG)

TOPIC_NAME = 'test-topic'
sleepTime = 1
PORT = '9093'

producer = KafkaProducer(
    # bootstrap_servers=['localhost:9092'],
    bootstrap_servers=['localhost:9093'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

print('Connected to Kafka')

for e in range(10):
    data = {'number': e}
    print('Sending {} to Kafka'.format(e))
    future = producer.send(TOPIC_NAME, value=data)
    
    r_meta = None
    try:
        r_meta = future.get(timeout=10)
    except KafkaError as e:
        print('Kafka error: ', e)
    
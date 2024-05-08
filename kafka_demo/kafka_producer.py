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
    bootstrap_servers=['localhost' + PORT],
    # value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

print('Connected to Kafka')

future = producer.send(TOPIC_NAME, b'testVal', b'testKey')

print('Sent the value')

record_metadata = None
# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError as e:
    # Decide what to do if produce request failed...
    print('Kafka error: ', e)

#
# for e in range(10):
#     data = {'number': e}
#     print('Sending {} to Kafka'.format(e))
#     producer.send(TOPIC_NAME, value=data)
from json import loads
from kafka import KafkaConsumer

TOPIC_NAME = 'test-topic'
CONSUMER_GRP = 'my-group'
PORT = '9093'

consumer = KafkaConsumer(
    TOPIC_NAME,
    # bootstrap_servers=['localhost:9092'],
    bootstrap_servers=['localhost:' + PORT],
    group_id=CONSUMER_GRP,
    # value_deserializer=lambda x: loads(x.decode('utf-8'))
    )

print('Connected to Kafka')

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

# for message in consumer:
#     message = message.value
#     print('Received value: {}'.format(message))

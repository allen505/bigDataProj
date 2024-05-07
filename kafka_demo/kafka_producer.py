from time import sleep
from json import dumps
from kafka import KafkaProducer

TOPIC_NAME = 'vidRecommender'
sleepTime = 1

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

print('Connected to Kafka')

for e in range(10):
    data = {'number': e}
    print('Sending {} to Kafka'.format(e))
    producer.send(TOPIC_NAME, value=data)
    print('Sleeping for {} seconds'.format(sleepTime))
    sleep(sleepTime)

# Reference https://kafka-python.readthedocs.io/en/master/usage.html

from kafka import KafkaConsumer
import json
import logging


logger = logging.getLogger(__name__)
# enable the debug logger if you want to see ALL of the lines
logging.basicConfig(level=logging.INFO)


# Creating Kafka Consumer
# Consumes Kafka messages

listBootstrapServer = ['127.0.0.1:9092']

consumer = KafkaConsumer('Learning_Kafka_1',
                         bootstrap_servers=listBootstrapServer,
                         auto_offset_reset='earliest',
                         value_deserializer=lambda m: json.loads(m.decode('ascii')),
                         consumer_timeout_ms=1000000,
                         group_id='My-first-app')


for message in consumer:
    print("topic=%s partition=%d offset=%d key=%s value=%s" % (message.topic, message.partition,
                                                               message.offset, str(message.key),
                                                               message.value))


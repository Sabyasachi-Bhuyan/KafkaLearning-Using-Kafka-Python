from kafka import KafkaProducer
from json import dumps
import logging


listBootstrapServer = ['127.0.0.1:9092']

producer = KafkaProducer(bootstrap_servers=listBootstrapServer,
                         value_serializer=lambda x: dumps(x).encode('utf-8'))


def on_send_success(record_metadata):
    print("Topic : " + record_metadata.topic)
    print("Partition : " + str(record_metadata.partition))
    print("Offset : " + str(record_metadata.offset))


# On Error
def on_send_error(excp):
    logging.error('I am an errback', exc_info=excp)


# Same Key always goes to same partition
for i in range(10):
    message = "Hello" + str(i)
    key = b'id_' + bytes(i)
    producer.send('Learning_Kafka_1', key=key, value=message).add_callback(on_send_success).add_errback(on_send_error)


# Flush data
producer.flush()

# Close producer
producer.close()



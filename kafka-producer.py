from kafka import KafkaProducer
from json import dumps


# Create the Producer with Properties
# Send Data

listBootstrapServer = ['127.0.0.1:9092']

producer = KafkaProducer(bootstrap_servers=listBootstrapServer,
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

message = 'Testing Kafka'
print(message)
producer.send('Learning_Kafka_1', message)

# Flush data
producer.flush()

# Close producer
producer.close()



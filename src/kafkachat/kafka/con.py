from kafka import KafkaConsumer
from json import loads

consumer  = KafkaConsumer(
    'abcdefg',
    bootstrap_servers = ["localhost:9092"],
    value_serializer=lambda x: loads(x).encode('utf-8'),
    consumer_timeout_ms=5000
    )


print('[Start] get consumer')

for msg in consumer:
    print(msg)

print('[End] get consumer')
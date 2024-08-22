from kafka import KafkaProducer, KafkaConsumer
import json
import threading
import time
import datetime

def reciver():

    consumer = KafkaConsumer(
    'chat',
    bootstrap_servers=['ec2-3-38-102-55.ap-northeast-2.compute.amazonaws.com:9092'],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    # group_id=f'chat-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    
    try:
        for m in consumer:
            data = m.value
            print(f"{data['name']}: {data['message']} (받은 시간 : {m.timestamp // 1000})")
    except KeyboardInterrupt:
        print("채팅 종료")
    finally:
        consumer.close()

def sender(username):
    producer = KafkaProducer(
    bootstrap_servers=['ec2-3-38-102-55.ap-northeast-2.compute.amazonaws.com:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    while True:
        message = input("You : ")

        data = {'name':username, 'message': message, 'time': time.time()}

        if message == 'exit':
            producer.close()
            break

        producer.send('chat', value=data)
        producer.flush()

if __name__ == "__main__":
    print("채팅 프로그램 - 메시지 발신 및 수신")
    username = input("사용할 이름을 입력하세요 : ")

    consumer_thread = threading.Thread(target=reciver)
    producer_thread = threading.Thread(target=sender, args=(username,))

    consumer_thread.start()
    producer_thread.start()

    # consumer_thread.join()
    # producer_thread.join()


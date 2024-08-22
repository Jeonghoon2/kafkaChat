from kafka import KafkaProducer, KafkaConsumer
import json
import threading
import time
import sys
import datetime

def clear_screen():
    sys.stdout.write("\033[H\033[J")

messages = []

def receiver():
    global messages
    consumer = KafkaConsumer(
        'chat',
        bootstrap_servers=['ec2-3-38-102-55.ap-northeast-2.compute.amazonaws.com:9092'],
        auto_offset_reset='latest',
        enable_auto_commit=True,
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    
    try:
        for m in consumer:
            data = m.value
            # 수신된 메시지를 리스트에 추가
            messages.append(f"{data['username']}: {data['message']} (받은 시간 : {datetime.datetime.fromtimestamp(m.timestamp // 1000)})")
            
            # 화면을 지우고, 모든 메시지를 출력
            clear_screen()
            for message in messages:
                print(message)
            
            # 입력란을 하단에 고정
            sys.stdout.write("You: ")
            sys.stdout.flush()
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

        sys.stdout.write("You: ")
        sys.stdout.flush()
        message = input()
        data = {'username':username, 'message': message, 'time': time.time()}

        if message == 'exit':
            producer.close()
            break

        producer.send('chat', value=data)
        producer.flush()

if __name__ == "__main__":
    print("채팅 프로그램 - 메시지 발신 및 수신")
    username = input("사용할 이름을 입력하세요 : ")

    consumer_thread = threading.Thread(target=receiver)
    producer_thread = threading.Thread(target=sender, args=(username,))

    consumer_thread.start()
    producer_thread.start()

    # consumer_thread.join()
    # producer_thread.join()


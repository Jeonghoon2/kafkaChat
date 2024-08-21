# kafkaChat

### Develop Env
```
- python 3.8.19
- kafka_2.12-2.4.1
```

### 단방향 메시지
- [**Consumer-Chat**](https://github.com/Jeonghoon2/kafkaChat/blob/0.3/chat/src/kafkachat/kafka/cchat.py) : Kafka Topic에서 데이터를 읽어 오는 Consumer 역할을 합니다.
    ``` bash
    $ python cchat.py
    채팅 프로그램 - 메시지 수신
    메시지 대기 중 . . .
    hun:  (받은 시간 : 1724232545.370801)
    ```


- [**Producer-Chat**](https://github.com/Jeonghoon2/kafkaChat/blob/0.3/chat/src/kafkachat/kafka/pchat.py) : 사용자의 입력을 받아 Kafka Topic으로 메시지를 전송하는 Producer 역할을 합니다.
    ``` bash
    $ python cchat.py
    python pchat.py
    채팅 프로그램 - 메시지 발신자
    채팅에 사용하실 이름을 정해주세요 :  hun
    메시지를 입력하세요. (종료시 'exit' 입력)
    You : hi
    You : exit
    채팅이 종료되었습니다.
    ```


---

### [**Mission 1**] 여러 명이 사용 가능한 채팅은 어떻게 만들까?

#### **아이디어**
1. 새로운 파일 하나를 만든다. (MultiChat.py)
2. MultiChat.py 안에 **메시지를 받는 Consumer**와 **메시지를 보내는 Producer** 역할을 하는 함수를 만든다.
3. 내장 함수 **threading**을 사용하여 송신과 수신 함수를 동작 시킨다.

    ```python
    import threading

    # Exam
    def producer(username):
        pass

    def consumer():
        pass
    
    username = input("채팅방에서 사용할 이름을 입력해주세요 : ")
    thread_1 = threading.Thread(target = producer, arg = (username))
    thread_2 = threading.Thread(target = consumer, arg = ())

    thread_1.start()
    thread_2.start()
    ```

#### 예상 결과
하나의 프로세스에서 두 개의 쓰레드를 동시에 동작하게 함으로써, 하나의 쓰레드에서는 사용자의 입력을 받아 Kafka Topic으로 메시지를 전송하고, 다른 쓰레드에서는 Kafka Topic에서 메시지를 수신하여 실시간으로 채팅을 진행할 수 있습니다.



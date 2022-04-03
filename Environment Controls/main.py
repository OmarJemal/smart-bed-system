import threading
import datetime
import time
import json
from ControlSystem import SetAlarm
from kafka import KafkaConsumer

alarm_time = ""
previous_time = ""
sleep_data = ""
previous_sleep_data = ""


class AlarmThread(threading.Thread):
    def __init__(self, ThreadID, name):
        threading.Thread.__init__(self)
        self.ThreadID = ThreadID
        self.name = name

    def run(self):
        global previous_time
        while True:
          lock.aquire()
          if(alarm_time != previous_time):
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
          lock.release()
          time.sleep(10)


class SettingsThread(threading.Thread):
    def __init__(self, ThreadID, name):
        threading.Thread.__init__(self)
        self.ThreadID = ThreadID
        self.name = name

    def run(self):
        global alarm_time
        global previous_time
        while True:
          lock.aquire()
          lock2.aquire()
          if alarm_time > datetime.datetime.now().strftime("%H:%M:%S") & sleep_data == 1:
                
              SetAlarm(alarm_time)
              previous_time = alarm_time
              alarm_time = ""
          else:
              time.sleep(20)
          lock.release()
          lock2.release()
          time.sleep(20)


class KafkaListener(threading.Thread):
    def __init__(self, ThreadID, name):
        threading.Thread.__init__(self)
        self.ThreadID = ThreadID
        self.name = name
        self.init_kafka_consumer(self)


    # initialize the kafka consumer
    def init_kafka_consumer(self):
        self.consumer = KafkaConsumer(
            bootstrap_servers='10.0.0.188:9092',
            enable_auto_commit=True,
            #max_poll_interval_ms=5000,
            #max_poll_records=1,
            #auto_offset_reset='smallest',
            #consumer_timeout_ms=1000
        )

    def retrieveKafka(self):
        try:
            print("bootstrap connected: ", self.consumer.bootstrap_connected())

            print("poll results: ", self.consumer.poll())

            comsumer_topics = self.consumer.topics()

            print("topics: ", comsumer_topics)

            self.consumer.subscribe(topics=comsumer_topics)

            print(f"subscribed to {comsumer_topics}")
            print(f"subscriptipn : {self.consumer.subscription()}")

            for msg in self.consumer:
                print(msg)

        except Exception as e:
            print(f"exception was {e}")

    def run(self):
        global sleep_data
        while True:
          lock2.aquire()
          if change_in_kafka:
             sleep_data = self.retrieveKafka()
          else:
              time.sleep(10)
          lock2.release()
          time.sleep(10)


lock = threading.Lock()
lock2 = threading.Lock()

alarmWatchingThread = AlarmThread(1, "Alarm Watching Thread")
alarmSettingThread = SettingsThread(2, "Alarm Setting Thread")
kafkaListenerThread = KafkaListener(3, "Kafka Listener Thread")

alarmWatchingThread.start()
alarmSettingThread.start()
kafkaListenerThread.start()

alarmWatchingThread.join()
alarmSettingThread.join()
kafkaListenerThread.join()

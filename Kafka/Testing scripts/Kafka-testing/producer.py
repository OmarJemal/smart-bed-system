from time import sleep
from datetime import datetime
import json
import logging as log

from kafka import KafkaProducer
from kafka.errors import KafkaError

try:    
    producer = KafkaProducer(bootstrap_servers='localhost:19092', batch_size=0, retries=3)

    print("bootstrap connected: ", producer.bootstrap_connected())
except Exception as ex:
    print('Exception while connecting Kafka')
    print(str(ex))

def on_send_success(record_metadata):
    print("success")
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    print("error")
    log.error('I am an errback', exc_info=excp)
    # handle exception

# produce asynchronously with callbacks

counter = 0
while 1:
    
    print("reached 1")
    #producer.send('kafka-testing-topic', b'it works yessss')
    producer.send('kafka-testing-topic', f'it works yessss {counter}'.encode()).add_callback(on_send_success).add_errback(on_send_error)
    #future = producer.send('kafka-testing-topic', b'it works yessss')
    print("reached 2")
    producer.flush()
    print("reached 3")
    #producer.close()
    # Asynchronous by default

    # Block for 'synchronous' sends
    try:
        #record_metadata = future.get(timeout=10)
        pass
    except KafkaError as e:
        # Decide what to do if produce request failed...
        print(f"exception was {e}")
        pass
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    
    counter += 1
    print(f' current count is {counter}')
    #print(f' The metadata for the message is {record_metadata}')
   
    sleep(1) 
  
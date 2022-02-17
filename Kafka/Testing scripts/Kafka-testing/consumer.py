import json
 
from kafka import KafkaConsumer
#from pymongo import MongoClient


# Setup mongo connection
# client = MongoClient()
# db = client.metamorphosis
# metamorphosis = db.metamorphosis 

#consumer = KafkaConsumer('kafka-testing-topic',bootstrap_servers='localhost:30302')
consumer = KafkaConsumer(bootstrap_servers='localhost:19092',enable_auto_commit = True,
                     max_poll_interval_ms=5000,
                     max_poll_records=1,
                     #auto_offset_reset='smallest', 
                     #consumer_timeout_ms=1000
                     )

try:
    
    print("bootstrap connected: ",consumer.bootstrap_connected())

    print("poll results: ", consumer.poll())

    comsumer_topics = consumer.topics()

    print("topics: ", comsumer_topics)

    consumer.subscribe(topics=comsumer_topics)

    print(f"subscribed to {comsumer_topics}")
    print(f"subscriptipn : {consumer.subscription()}")
    
    for msg in consumer:
        print(msg)
        
except Exception as e:
    print(f"exception was {e}")


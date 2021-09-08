from kafka import KafkaConsumer
from json import loads
import ast
import pickle
import numpy as np
import os

BROKER = os.getenv('BROKER', 'localhost:9092')                                                                                               

consumer = KafkaConsumer(
    'tweets',
     bootstrap_servers=[BROKER],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group')

mm = pickle.load(open("models/model.sav", 'rb'))

for message in consumer:
    message = message.value
    message = message.decode('utf8').replace(" ", ',')
    message = ast.literal_eval(message)
    prediction = mm.predict(np.asarray([message]))
    print(prediction)

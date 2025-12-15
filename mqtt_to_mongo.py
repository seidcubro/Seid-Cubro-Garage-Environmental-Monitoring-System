import json
from datetime import datetime
import paho.mqtt.client as mqtt
from pymongo import MongoClient

BROKER = "url.s1.eu.hivemq.cloud"
PORT = 8883
USERNAME = "username"
PASSWORD = "password"
TOPIC = "sensor/dht11"

MONGO_URI = "mongo_uri"
DB_NAME = "iot_env"
COLLECTION = "readings"

mongo = MongoClient(MONGO_URI)
db = mongo[DB_NAME]
col = db[COLLECTION]

print("Connected to MongoDB Atlas")

def on_connect(client, userdata, flags, rc):
    client.subscribe(TOPIC)
    print("Subscribed to HiveMQ topic")

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    document = {
        "timestamp": datetime.utcnow(),
        "temperature": data["temperature"],
        "humidity": data["humidity"]
    }

    col.insert_one(document)
    print("Inserted:", document)

client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)
client.loop_forever()



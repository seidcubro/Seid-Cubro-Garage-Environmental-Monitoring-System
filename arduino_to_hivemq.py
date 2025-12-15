import serial
import json
import time
import paho.mqtt.client as mqtt

SERIAL_PORT = "COM3"
BAUD_RATE = 9600
BROKER = "eca20bedafe647028313f114982d0feb.s1.eu.hivemq.cloud"
PORT = 8883
USERNAME = "seidcubro"
PASSWORD = "220022Seid"
TOPIC = "sensor/dht11"

def on_connect(client, userdata, flags, rc):
    print("MQTT connect result code:", rc)

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()
client.on_connect = on_connect

print("Connecting to HiveMQ...")
client.connect(BROKER, PORT)

client.loop_start()
time.sleep(2)

print("Publishing Arduino data to HiveMQ...")

while True:
    raw = ser.readline()
    if not raw:
        continue

    print("RAW:", raw)

    try:
        line = raw.decode("utf-8").strip()

        if "Temperature" not in line or "Humidity" not in line:
            continue

        temp_str = line.split("Temperature (C):")[1].split(",")[0].strip()

        hum_str = line.split("Humidity:")[1].replace("%", "").strip()

        temperature = float(temp_str)
        humidity = float(hum_str)

        payload = {
            "temperature": temperature,
            "humidity": humidity
        }

        result = client.publish(TOPIC, json.dumps(payload))

        print("Published:", payload, "RC:", result.rc)

    except Exception as e:
        print("PARSE ERROR:", e)



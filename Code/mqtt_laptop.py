import paho.mqtt.client as mqtt
import sqlite3
import json

DB = 'sensordaten.db'

def on_connect(client, userdata, flags, rc):
    print("Verbunden mit MQTT-Broker")
    #client.subscribe("sensordaten_picow")    #Das Topic ist sensordaten_pico

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print("Empfangen:", data)
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO Messwerte (timestamp, temp, press, hum) VALUES (?, ?, ?, ?)",
              (data['timestamp'], data['temp'], data['press'], data['hum']))
    conn.commit()
    conn.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("172.20.10.2", 1883, 60)
client.subscribe("sensordaten_picow")

client.loop_forever()
from network import WLAN, STA_IF
from utime import sleep_ms
from umqtt_simple import MQTTClient
import json


MQTT_BROKER = "172.20.10.2"  # IP deines Laptops
CLIENT_ID = "pico"
TOPIC = b"sensordaten_pico"

def send_mqtt_data(timestamp, temp, press, hum):
    client = MQTTClient(CLIENT_ID, MQTT_BROKER)
    client.connect()
    payload = {
        "timestamp": timestamp,
        "temp": temp,
        "press": press,
        "hum": hum
    }
    msg = json.dumps(payload)
    client.publish(TOPIC, msg)
    client.disconnect()





"""
# Callback when a message is received
def sub_cb(topic, msg):
    print(f"Received: Topic={topic}, Message={msg}")

#print ("Test1")

# Setup MQTT client and connect to broker
client = MQTTClient("PicoW_sub", "172.20.10.2")  # IP des Rechners (individuell und auch nach Neustart oder je nach Netzwerk anders)
client.set_callback(sub_cb)
client.connect()

#print ("Test2")

# Subscribe to topic
client.subscribe(b"temperature")
print("Subscribed to temperature")
# Wait for messages
try:
    while True:
        client.wait_msg()  # Blocking wait
        # use client.check_msg() if you want non-blocking instead
except KeyboardInterrupt:
    print("Stopped by user")
    client.disconnect()
    """
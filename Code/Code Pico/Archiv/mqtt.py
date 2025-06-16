from network import WLAN, STA_IF
from utime import sleep_ms
from umqtt_simple import MQTTClient
#import connect_to_wifi as cw # eigenes ausgelagertes wifi skript vom Prof

#cw.check_wifi_connections()
#print('through connection overview')
# if connection established, this can be commented out
#cw.connect_to_wifi(ssid,pw)

# Callback when a message is received
def sub_cb(topic, msg):
    print(f"Received: Topic={topic}, Message={msg}")

print ("Test1")

# Setup MQTT client and connect to broker
client = MQTTClient("PicoW_sub", "172.20.10.2")  # IP des Rechners (individuell und auch nach Neustart oder je nach Netzwerk anders)
client.set_callback(sub_cb)
client.connect()

print ("Test2")

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
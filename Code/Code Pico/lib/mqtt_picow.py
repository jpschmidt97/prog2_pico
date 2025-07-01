from umqtt_simple import MQTTClient
import json

MQTT_BROKER = "172.20.10.2"  # IP deines MQTT-Brokers (z. B. Laptop)
CLIENT_ID = "pico"
TOPIC = b"sensordaten_picow"

client = None  # globale MQTTClient-Instanz

def mqtt_connect():
    global client
    if client is None:
        try:
            client = MQTTClient(CLIENT_ID, MQTT_BROKER)
            client.connect()
            print("MQTT verbunden")
        except OSError as e:
            print("MQTT Verbindungsfehler:", e)


def send_mqtt_data(timestamp, temp, press, hum):
    global client
    if client is None:
        mqtt_connect()

    payload = {
        "timestamp": timestamp,
        "temp": temp,
        "press": press,
        "hum": hum
    }

    msg = json.dumps(payload)

    try:
        client.publish(TOPIC, msg)
    except OSError:
        print("MQTT Verbindungsproblem – reconnect wird versucht")
        try:
            client.disconnect()  # Falls nötig, Verbindung zurücksetzen
        except:
            pass
        client = None
        mqtt_connect()
        try:
            client.publish(TOPIC, msg)
        except Exception as e:
            print("MQTT Senden fehlgeschlagen:", e)


# Getter-Funktion für Zugriff in main.py – wichtig, da client erst nach mqtt_connect() gültig ist
def get_mqtt_client():
    global client
    return client

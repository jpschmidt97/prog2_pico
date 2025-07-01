# main.py - finale Version

import network
import uasyncio as asyncio
from lib.sensor_manager import SensorManager     # SensorManager-Klasse ersetzt direkte Sensorfunktion
from lib.LED import led_test, ventilation_task
from lib.oled import oled_test, oled
from lib.datalogger import init_memory, save_messure
from lib.mqtt_picow import mqtt_connect, send_mqtt_data, get_mqtt_client
import ntptime
import time

#WLAN Definition
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Intervall-Einstellungen
MESS_INTERVALL = 5    # Sekunden zwischen den Messungen
OLED_REFRESH = 5      # Sekunden zwischen OLED-Updates

# Shared State für Sensordaten
sensor_data = {
    "temp": 0.0,
    "press": 0.0,
    "hum": 0.0
}

# SensorManager-Instanz erstellen
sensor_mgr = SensorManager()    # Neue Klasse verwaltet die Sensorwerte inkl. Zeitstempel

# MQTT-Nachrichten-Callback
def mqtt_message_callback(topic, msg):
    global MESS_INTERVALL
    try:
        if topic.decode() == "picow/command":
            payload = msg.decode()
            if payload.startswith("set_interval:"):
                value = int(payload.split(":")[1])
                if 1 <= value <= 3600:
                    MESS_INTERVALL = value
                    print(f"[MQTT] Neues Messintervall empfangen: {value} Sekunden")
                else:
                    print("[MQTT] Ungültiges Intervall empfangen (muss 1-3600 sein)")
    except Exception as e:
        print(f"[MQTT] Fehler beim Verarbeiten der Nachricht: {e}")


async def startup_tests():
    #Führt die Hardware-Tests nacheinander aus:
    #- LED-Test (blockierend)
    #- OLED-Test (blockierend)

    led_test()       # blockiert, bis der LED-Test fertig ist
    oled_test()      # blockiert, bis der OLED-Test fertig ist
    await asyncio.sleep(0)  # einmal zum Scheduler zurückgeben


async def sync_time():
    # Warte, bis WLAN verbunden ist
    while not wlan.isconnected():
        await asyncio.sleep(0.5)
    try:
        ntptime.settime()
        print("Uhrzeit synchronisiert.")
    except:
        print("Zeit konnte nicht synchronisiert werden.")


def get_timestamp(offset_hours = 2):
    t = time.localtime(time.time() + offset_hours * 3600)
    return f"{t[2]:02d}.{t[1]:02d}.{t[0]:04d} {t[3]:02d}:{t[4]:02d}:{t[5]:02d}"


async def sensor_task():
    #Liest kontinuierlich Sensordaten, speichert sie lokal und druckt sie in die Konsole.

    init_memory()    #der Sensor wird einmalig initialisiert
    while True:
        sensor_mgr.read()   # neue Methode ruft die Sensorwerte ab und speichert sie intern
        t, p, h, timestamp = sensor_mgr.get_values()   # Werte + Zeitstempel abrufen
        sensor_data["temp"] = t
        sensor_data["press"] = p
        sensor_data["hum"] = h
        print(f"[{timestamp}] Temp: {t:.2f} °C, Druck: {p:.2f} hPa, Feuchte: {h:.2f} %")
        #save_messure(t, p, h)    #die aktuellen Messwerte werden in einer .csv Datei gespeichert
        if wlan.isconnected():    #WLAN-Verbindung prüfen
            send_mqtt_data(timestamp, t, p, h)
        else:
            print("Kein WLAN - MQTT wird nicht gesendet")
        await asyncio.sleep(MESS_INTERVALL)


async def oled_task():
    #Aktualisiert das OLED-Display mit den zuletzt gelesenen Sensordaten

    while True:
        oled.fill(0)

        if wlan.isconnected():
            oled.text("WLAN verbunden", 0, 0)
        else:
            oled.text("KEIN WLAN", 0, 0)

        oled.text(f"Temp: {sensor_data['temp']:.1f} C", 0, 16)
        oled.text(f"Druck: {sensor_data['press']:.0f} hPa", 0, 32)
        oled.text(f"Feuchte: {sensor_data['hum']:.1f} %", 0, 48)
        oled.show()
        await asyncio.sleep(OLED_REFRESH)


def get_sensor_data():
    return sensor_data["temp"], sensor_data["hum"]


async def mqtt_loop_task():
    # Hört dauerhaft auf MQTT-Nachrichten
    while True:
        try:
            client = get_mqtt_client()
            if client:
                client.check_msg()
        except Exception as e:
            print(f"[MQTT] Fehler beim Empfang: {e}")
        await asyncio.sleep(1)


async def main():
    # Startup-Initialisierung
    await startup_tests()

    #akteulle Zeit
    await sync_time()

    #MQTT-Verbindung einmal herstellen
    mqtt_connect()
    client = get_mqtt_client()
    if client:
        client.set_callback(mqtt_message_callback)
        client.subscribe("picow/command")
    else:
        print("[MQTT] Kein gültiger MQTT-Client verfügbar!")

    # Tasks parallel starten
    task1 = asyncio.create_task(sensor_task())
    task2 = asyncio.create_task(oled_task())
    task3 = asyncio.create_task(ventilation_task(get_sensor_data))
    task4 = asyncio.create_task(mqtt_loop_task())

    # Event-Loop läuft, bis du manuell mit CTRL+C abbrichst
    await asyncio.gather(task1, task2, task3, task4)

# uasyncio-Event-Loop starten
asyncio.run(main())

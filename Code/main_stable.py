# main.py - uasyncio Version

import network
import uasyncio as asyncio
from lib.temp_messung import bme_messure
from lib.LED import led_test
from lib.oled import oled_test, oled
from lib.datalogger import init_memory, save_messure


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

async def startup_tests():
    #Führt die Hardware-Tests nacheinander aus:
    #- LED-Test (blockierend)
    #- OLED-Test (blockierend)
    
    led_test()       # blockiert, bis der LED-Test fertig ist
    oled_test()      # blockiert, bis der OLED-Test fertig ist
    await asyncio.sleep(0)  # einmal zum Scheduler zurückgeben

async def sensor_task():
    #Liest kontinuierlich Sensordaten, speichert sie lokal und druckt sie in die Konsole.
    
    init_memory()    #der Sensor wird einmalig initialisiert
    while True:
        t, p, h = bme_messure()
        sensor_data["temp"] = t
        sensor_data["press"] = p
        sensor_data["hum"] = h
        print(f"Temp: {t:.2f} °C, Druck: {p:.2f} hPa, Feuchte: {h:.2f} %")
        #save_messure(t, p, h)    #die aktuellen Messwerte werden in einer .csv Datei gespeichert
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

async def main():
    # Startup-Initialisierung
    await startup_tests()

    # Tasks parallel starten
    task1 = asyncio.create_task(sensor_task())
    task2 = asyncio.create_task(oled_task())

    # Event-Loop läuft, bis du manuell mit CTRL+C abbrichst
    await asyncio.gather(task1, task2)

# uasyncio-Event-Loop starten
asyncio.run(main()) 
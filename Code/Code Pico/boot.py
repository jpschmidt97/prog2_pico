# boot.py – Wird beim Start des Pico W als Erstes ausgeführt

import network
from utime import sleep

print("Pico W wurde gestartet, boot.py wird ausgeführt - 10 Sekunden Wartezeit")
#sleep(10)  # Warten, um bei Start mögliche Konsolenausgaben zu sehen bzw. Code zu löschen

def connect_wifi(ssid, password):
    print(f"Verbindung zu WLAN '{ssid}' wird hergestellt...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    sleep(1)

    if not wlan.isconnected():
        wlan.connect(ssid, password)
        timeout = 15
        while not wlan.isconnected() and timeout > 0:
            sleep(1)
            timeout -= 1
            print(f"  ...warte ({15 - timeout}s)")

    if wlan.isconnected():
        print("Verbunden mit:", ssid)
        print("IP-Adresse:", wlan.ifconfig()[0])
    else:
        print("Verbindung fehlgeschlagen, nach 15 Sekunden abgebrochen.")
        wlan.disconnect()  # Aktiv trennen, damit keine weitere Verbindung versucht wird
        wlan.active(False) # WLAN-Modul deaktivieren
        
try:
    # Entweder Heimnetz oder Hotspot
    #connect_wifi("Vodafone-B3C7", "XVqMLiVMfVe763RP")
    connect_wifi("iPhone_Pascale", "qwertzuiop")

except Exception as e:
    print("Fehler beim Aufbau der WLAN-Verbindung:", e)
    sleep(10)  # Zeit zur Fehlersuche

print("boot.py wurde erfolgreich ausgeführt.")
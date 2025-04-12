#boot.py - wird als aller erstes beim Start des Pico W ausgeführt

import network
import time

def connect_wifi():
    print('Verbindung wird hergestellt...')
    ssid = "Vodafone-B3C7"
    password = "XVqMLiVMfVe763RP"
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Verbindung wird weiterhin hergestellt...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            time.sleep(1)
    print('Verbunden mit:', ssid)
    print('IP-Adresse:', wlan.ifconfig()[0])

# Aufruf der Funktion, um WLAN zu verbinden
connect_wifi()

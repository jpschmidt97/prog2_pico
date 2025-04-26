#boot.py - wird als aller erstes beim Start des Pico W ausgeführt

import network
from utime import sleep

sleep(5) #Warten um Ausgabe in Konsole zu sehen


def connect_wifi_home(): #Funktion zur Verbindung mit dem WLAN zu Hause
    print('Verbindung wird hergestellt...')
    ssid = "Vodafone-B3C7"
    password = "XVqMLiVMfVe763RP"
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(ssid, password)
        timeout = 15
        while not wlan.isconnected() and timeout > 0:
            sleep(1)
            timeout -= 1
    if wlan.isconnected():
        print('Verbunden mit:', ssid)
        print('IP-Adresse:', wlan.ifconfig()[0])
    else:
        print('Verbindung fehlgeschlagen.')
    

def connect_wifi_iphone(): #Funktion zur Verbindung mit dem WLAN zu Hause
    print('Verbindung wird hergestellt...')
    ssid = "iPhone_Pascale"
    password = "qwertzuiop"
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(ssid, password)
        timeout = 15
        while not wlan.isconnected() and timeout > 0:
            sleep(1)
            timeout -= 1
    if wlan.isconnected():
        print('Verbunden mit:', ssid)
        print('IP-Adresse:', wlan.ifconfig()[0])
    else:
        print('Verbindung fehlgeschlagen.')
    


#connect_wifi_home()  # Mit WLAN zu Hause verbinden
    
#connect_wifi_iphone()  # Mit mobilem HotSpot auf iPhone verbinden

print("boot.py wurde erfolgreich ausgeführt.")
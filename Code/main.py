#main.py - wird autom. ausgeführt, nachdem die boot.py vollständig ausgeführt wurde

#Unterprogramme werden im Ordner /lib/ abgelegt und von dort aufgerufen
#Aufrufen von Programmen aus /lib/ mit dem Befehl: import lib.ProgrammName
    
#-------------------------------------------------------------------------------------------------      

print("main.py wurde gestartet.")

import machine
from utime import sleep
import _thread  # Bibliothek für Multitasking


from lib.temp_messung import bme_messure    #Import Funktion bme_messure
from lib.LED import led_test    #Import LED Test Funktion
from lib.oled import oled_test, oled_update_thread

#kurze Hardware-Tests durchlaufen lassen:
_thread.start_new_thread(led_test, ())    # Starten des LED-Tests in einem neuen Thread
oled_test()    #startet den OLED Test - dadurch warten bis dieser durchgelaufen ist


#Stop-Funktion für die main.py:
running = True    #setzt eine Variable auf True - soll später als stop Möglichkeit genutzt werden

def stop_thread():
    global running
    while running:
        befehl = input()
        if befehl.strip().lower() == "stop":
            print("Stop-Befehl erhalten. Beende das Programm...")
            running = False

_thread.start_new_thread(stop_thread, ())








#BME Sensor Daten

#Speichern der aktuellen Messwerte in folgende Variablen
temp_c = 0
pressure_hpa = 0
humidity_percent = 0

#Abruf der Sensordaten in vorgegebenen Intervall
mess_int = 5   #Messung der Werte alle int Sekunden

def messure_thread(): #Funktion liest Werte aus der Mess-Funktion bme_messure() aus und gibt diese in der Konsole aus
    global temp_c, pressure_hpa, humidity_percent    #in globale Variablen schreiben
    while True:
        #Werte aus der Funktion auslesen
        temp_c, pressure_hpa, humidity_percent = bme_messure()
        
        #Ausgabe in Konsole - später evtl. über OLED
        print(f"Temperatur: {temp_c:.2f} °C")
        print(f"Luftdruck:  {pressure_hpa:.2f} hPa")
        print(f"Feuchte:    {humidity_percent:.2f} %")
        print("-" * 30)    
        
        sleep(mess_int)   # mess_int Sekunden warten
        
  

#_thread.start_new_thread(messure_thread, ())    #neuen Thread mit Endlosschleife starten um permanente Messung durchzuführen







#OLED Display - Ausgabe aktueller Messwerte/Sensordaten

_thread.start_new_thread(oled_update_thread, (lambda: (temp_c, pressure_hpa, humidity_percent),))    #Thread mit Definition der zu Übergebenden Werte






#Speicherung der Messdaten lokal auf dem Pico W:
from lib.datalogger import init_memory, save_messure

# Initialisierung
init_memory()

def messure_thread_local(): #Funktion liest Werte aus der Mess-Funktion bme_messure() aus und gibt diese in der Konsole aus
    global temp_c, pressure_hpa, humidity_percent    #in globale Variablen schreiben
    while True:
        #Werte aus der Funktion auslesen
        temp_c, pressure_hpa, humidity_percent = bme_messure()
        
        save_messure(temp_c, pressure_hpa, humidity_percent) #Speicherung der Messwerte   
        
        sleep(mess_int)   # mess_int Sekunden warten




_thread.start_new_thread(messure_thread_local, ())    #neuen Thread mit Endlosschleife starten um permanente Messung durchzuführen
      















while running: #main.py läuft solange, bis ein "stop" in die Konsole eingegeben wird
    time.sleep(1)

print("Programm wurde erfolgreich beendet.")

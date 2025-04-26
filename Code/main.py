#main.py - wird ausgeführt, nachdem die boot.py ausgeführt wurde

#Unterprogramme werden im Ordner /lib/ abgelegt und von dort aufgerufen
#Aufrufen von Programmen aus /lib/ mit dem Befehl: import lib.ProgrammName
    #in den Unterprogrammen in /lib/ wird mittels Threading gearbeitet
    #dadurch läuft die main.py parallel weiter zu den Unterprogrammen
    #Beispielprogramm:
#        import machine
#        import time
#        import _thread  # Modul für Threads
#
#        # Funktion zum Blinken der LED
#        def blink_led(pin_number):
#            led = machine.Pin(pin_number, machine.Pin.OUT)
#            while True:
#                led.toggle()
#                time.sleep(1)
#
#       # Starte den Blink-Thread
#        _thread.start_new_thread(blink_led, (15,))
#        #die Kommas sind wichtig, da diese zum einen die 15 als Tupel und blink_LED als Funktion an den Thread übergeben
      
      
      

print("main.py wurde gestartet.")

#import lib.RGB_LED_test
from lib.temp_messung import bme_messure


#BME Sensor Daten

#Speichern der aktuellen Messwerte in folgende Variablen
temperature = 0
pressure = 0
humidity = 0

#Abruf der Sensrdaten in vorgegebenen Intervall
int = 5   #Messung der Werte alle int Sekunden

def messure_thread():
    global temperature, pressure, humidity
    while True:
        #Werte aus der Funktion auslesen
        temperature, pressure, humidity = bme_messure()
        
        #Ausgabe in Konsole - später evtl. über OLED
        print(f"Temperatur: {temperatur:.2f} °C")
        print(f"Luftdruck:  {druck:.2f} hPa")
        print(f"Feuchte:    {feuchte:.2f} %")
        print("-" * 30)    
        
        time.sleep(int)   # int Sekunden warten



# Starten des LED-Tests in einem neuen Thread
_thread.start_new_thread(led_test, ())

print("Threading funktioniert.")
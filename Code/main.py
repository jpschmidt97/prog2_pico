#main.py - wird ausgeführt, nachdem die boot.py ausgeführt wurde

#Unterprogramme werden im Ordner /lib/ abgelegt und von dort aufgerufen
#Aufrufen von Programmen aus/lib/ mit dem Befehl: import lib.ProgrammName
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

import lib.RGB_LED_test

print("Threading funktioniert.")
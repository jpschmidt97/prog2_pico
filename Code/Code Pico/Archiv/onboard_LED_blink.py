import machine
import utime

# Auf dem Pico W ist die interne LED über den Namen "LED" ansprechbar.
led = machine.Pin("LED", machine.Pin.OUT)

while True:
    led.toggle()       # Schaltet die LED um (an/aus)
    utime.sleep(0.5)   # Pause von 0,5 Sekunden
#LED.py - Programm zur Ansteuerung der SMD RGB LED - (GND,R;G;B - Pin)

#-----------------------------------------------------------------------------

from machine import Pin, PWM
from utime import sleep
import uasyncio as asyncio


# Pin festlegen und definiert (je nach dem wo angeschlossen)
red_led = PWM(Pin(13))
green_led = PWM(Pin(14))
blue_led = PWM(Pin(15))

#PWM auf 1000 setzen
for pwm in (red_led, green_led, blue_led):
    pwm.freq(1000)

def set_color(r, g, b):
    # r, g, b: Werte von 0 (aus) bis 65535 (volle Helligkeit) - Mischen von Farben möglich
    red_led.duty_u16(r)
    green_led.duty_u16(g)
    blue_led.duty_u16(b)

#Definition der Farben als Variablem , ACHTUNG: wird als Tupel übergeben, daher beim verwenden mit *red entpacken
red = (65535, 0, 0)         # Rot
yellow = (65535, 25000, 0)  # Gelb
green = (0, 65535, 0)       # Grün
blue = (0, 0, 65535)        # Blau
white = (65535, 65535, 65535)  # Weiß
off = (0, 0, 0)             # Aus


def led_test():
    print("LED Test wird ausgeführt.")

    for i in range(2):
        t=0.3
        set_color(*red)          # Rot
        sleep(t)
        set_color(*yellow)       # Gelb
        sleep(t)
        set_color(*green)        # Grün
        sleep(t)
        set_color(*white)        # Weiß
        sleep(t)
        set_color(*off)          # Aus
        sleep(t)
 
    print("LED Test beendet.")
    


def show_ventilation_recommendation(temp, hum):
    """
    LED permanent auf Rot/Gelb/Grün je nach Sensorwert:
    - Rot: Feuchte > 60% oder Temp > 28°C
    - Gelb: Feuchte 50-60% oder Temp 25-28°C
    - Grün: Feuchte < 50% und Temp < 25°C
    """
    if hum > 60 or temp > 28:
        set_color(*red)
    elif 50 < hum <= 60 or 25 <= temp <= 28:
        set_color(*yellow)
    else:
        set_color(*green)

async def ventilation_task(get_sensor_data_callback):
    """
    Async-Task:
    - Alle 5 Sekunden: LED permanent entsprechend Sensorwerten aktualisieren
    - Alle 60 Minuten: Rote LED für 5 Minuten als Lüftungserinnerung
    """
    while True:
        # 60-Minuten Zyklus
        for _ in range(720):  # 720 * 5s = 3600s = 60 Minuten
            temp, hum = get_sensor_data_callback()
            show_ventilation_recommendation(temp, hum)
            await asyncio.sleep(5)

        # 5 Minuten rote Erinnerung
        print("Lüftungserinnerung: Bitte lüften! (rote LED 5 min)")
        for _ in range(60):  # 60 * 5s = 300s = 5 Minuten
            set_color(*red)
            await asyncio.sleep(5)

        # Danach geht es wieder in die permanente Anzeige zurück (nächster Loop)


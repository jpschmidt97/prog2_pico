#Programm zur Ansteuerung einer SMD LED (GND,R;G;B - Pin)
from machine import Pin, PWM
from utime import sleep
import machine
import utime


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



while True:
    set_color(*red)          # Rot
    sleep(1)
    set_color(*yellow)       # Gelb
    sleep(1)
    set_color(*green)        # Grün
    sleep(1)
    set_color(*white)         # Blau
    sleep(1)
    set_color(*off)          # Aus
    sleep(2)
    
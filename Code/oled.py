#oled.py

from machine import Pin, I2C
from lib import sh1106
from utime import sleep

# globale I2C Initialisierung (I2C0 auf GP0=SDA, GP1=SCL)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
oled = sh1106.SH1106_I2C(128, 64, i2c, addr=0x3c)

# Bildschirm reseten
oled.fill(0)


#Funktion OLED-Test:
def oled_test():
    oled.fill(0)
    oled.text("OLED Test OK", 0, 0)
    oled.text("-_-_-_-_-_-_", 0, 16)
    oled.show()
    print("OLED-Test wird ausgeführt.")
    sleep(4)
    oled.fill(0)
    oled.show()

# Funktion: OLED Ausgabe der Sensorwerte
def oled_update_thread(get_sensorwerte_callback):
    while True:
        # Sensorwerte abrufen
        temperature, pressure, humidity = get_sensorwerte_callback()

        # OLED Display aktualisieren
        oled.fill(0)
        oled.text("akt. Messdaten:", 0, 0)
        oled.text(f"Temp.: {temperature:.1f} C", 0, 16)
        oled.text(f"Druck: {pressure:.0f} hPa", 0, 32)
        oled.text(f"Feuchte: {humidity:.1f} %", 0, 48)
        oled.show()

        # Alle 5 Sekunden refreshen -> neue Ausgabe auf OLED
        sleep(5)
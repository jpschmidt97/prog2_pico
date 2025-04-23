from machine import Pin, I2C
import sh1106
import time

# I2C Initialisierung (I2C0 auf GP0=SDA, GP1=SCL)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

# OLED Display initialisieren
oled = sh1106.SH1106_I2C(128, 64, i2c, addr=0x3c)

# Bildschirm löschen
oled.fill(0)

# Text anzeigen
oled.text("Hello Pico W!", 0, 0)
oled.text("SH1106 OLED :)", 0, 16)

# Ausgabe aktualisieren
oled.show()
#temp_messung.py


from machine import Pin, I2C
from utime import sleep
from lib import bme280    #Import aus dem Ordner lib

# I2C auf GP0 (SDA) und GP1 (SCL) initialisieren
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

# BME280 initialisieren
sensor = bme280.BME280(i2c=i2c, address=0x76)

# Definition der Messung
def bme_messure():
    
    temp, pressure, humidity = sensor.read_compensated_data()
    
    # sensorspezifische Umrechnung in lesbare Werte
    temp_c = temp / 100       # z.B. 2325 -> 23.25 °C
    pressure_hpa = pressure / 25600  # z.B. 101325 -> ~1013.25 hPa
    humidity_percent = humidity / 1024  # z.B. 4512 -> 4.4%

    # Ausgabe im Terminal
    #print(f"Aktuelle Temperatur: {temp_c:.2f} °C")
    #print(f"Luftdruck: {pressure_hpa:.2f} hPa")
    #print(f"Luftfeuchtigkeit: {humidity_percent:.2f} %")
    #print("-" * 30)
        
    #Rückgabe der Werte aus der Schleife
    return temp_c, pressure_hpa, humidity_percent
    
    


from machine import Pin, I2C
import time
import bme280

# I2C auf GP0 (SDA) und GP1 (SCL) initialisieren
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

# BME280 initialisieren
sensor = bme280.BME280(i2c=i2c, address=0x76)

# Endlosschleife zur Messung
while True:
    temp, pressure, humidity = sensor.read_compensated_data()
    
    # Umrechnung in lesbare Werte
    temp_c = temp / 100       # z.B. 2325 -> 23.25 °C
    pressure_hpa = pressure / 25600  # z.B. 101325 -> ~1013.25 hPa
    humidity_percent = humidity / 1024  # z.B. 4512 -> 4.4%

    # Ausgabe im Terminal
    print("Temperatur: {:.2f} °C".format(temp_c))
    print("Luftdruck: {:.2f} hPa".format(pressure_hpa))
    print("Luftfeuchtigkeit: {:.2f} %".format(humidity_percent))
    print("-" * 30)
    
    time.sleep(2)
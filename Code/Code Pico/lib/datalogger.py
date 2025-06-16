#datalogger.py - Programm zur Speicherung der Messdaten lokal auf dem Pico W als "Standalone Lösung"

from utime import sleep, ticks_ms, ticks_diff

# Name der Datei, wo die Daten gespeichert werden
filename = "messwerte.csv"

# Startzeit merken (in Millisekunden)
startzeit = ticks_ms()

# Funktion zum Initialisieren der Datei (nur 1x am Start)
def init_memory():
    try:
        with open(filename, "x") as f:
            # CSV-Header schreiben, falls Datei neu angelegt wird
            f.write("Zeitstempel,Temperatur,Luftdruck,Feuchte\n")
    except OSError:
        # Datei existiert bereits, nichts tun
        pass

# Funktion zum Erzeugen des aktuellen Zeitstempels seit Start
def get_time_since_start():
    vergangen = ticks_diff(ticks_ms(), startzeit) // 1000  # Sekunden
    stunden = vergangen // 3600
    minuten = (vergangen % 3600) // 60
    sekunden = vergangen % 60
    return "{:02d}:{:02d}:{:02d}".format(stunden, minuten, sekunden)

# Funktion zum Speichern eines Messwertes
def save_messure(temp_c, pressure_hpa, humidity_percent):
    time_string = get_time_since_start()

    with open(filename, "a") as f:
        f.write(f"{time_string},{temp_c:.2f},{pressure_hpa:.2f},{humidity_percent:.2f}\n")
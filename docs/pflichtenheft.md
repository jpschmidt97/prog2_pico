# Pflichtenheft: Indoor Wetterstation

## 1. Projektbeschreibung

Die Indoor Wetterstation soll die Raumluftqualität überwachen, indem sie die **Luftfeuchtigkeit**, **Temperatur** und **Luftdruck** misst. Diese Daten werden an einen Server gesendet, gespeichert und über ein **HTML-basiertes User-Interface** angezeigt. Das System wird mit einem **Raspberry Pi Pico W Mikrocontroller** umgesetzt und stellt sicher, dass die erfassten Daten langfristig in einer Datenbank gespeichert werden.

## 2. Ziel des Projekts

Ziel ist es, eine funktionale Wetterstation zu entwickeln, die folgende Anforderungen erfüllt:
- Erfassung der Raumluftdaten (Temperatur, Luftfeuchtigkeit und Luftdruck).
- Kommunikation der gesammelten Daten mit einem Server.
- Langfristige Speicherung der Daten in einer Datenbank.
- Bereitstellung eines Benutzer-Interfaces zur Visualisierung der Daten.

## 3. Funktionale Anforderungen

### 3.1 Messung der Raumluftparameter
- **Temperatur**: Die Temperatur soll in Grad Celsius erfasst werden.
- **Luftfeuchtigkeit**: Die Luftfeuchtigkeit soll in Prozent gemessen werden.
- **Luftdruck**: Der Luftdruck soll in hPa erfasst werden.

### 3.2 Mikrocontroller
- Der Mikrocontroller **Raspberry Pi Pico W** wird für die Datenerfassung und -übertragung verwendet.

### 3.3 Multitasking
- Das Projekt muss ein einfaches Multitasking-Konzept implementieren, wobei unabhängige Aufgaben gleichzeitig ausgeführt werden können, z. B. das Auslesen der Sensoren und das Senden von Daten an den Server.

### 3.4 Kommunikation
- Die Messdaten sollen regelmäßig an einen Server gesendet werden.
- Der Mikrocontroller kommuniziert über **Wi-Fi** mit dem Server.

### 3.5 Datenspeicherung
- Die Messdaten sollen langfristig in einer Datenbank gespeichert werden, um eine historische Analyse der Raumluftqualität zu ermöglichen.
- Es wird eine einfache **SQL-basierte Datenbank** (z. B. **MySQL** oder **SQLite**) verwendet.

### 3.6 Benutzer-Interface
- Ein **HTML**-basiertes User-Interface wird entwickelt, um die Daten anzuzeigen.
- Das Interface soll die aktuellen Werte für Temperatur, Luftfeuchtigkeit und Luftdruck visualisieren.

### 3.7 Qualitätssicherung
- Der Code muss dokumentiert werden, insbesondere durch den Einsatz von **Docstrings** für alle Funktionen und Klassen.
- Alle Codeänderungen sollen über **GitHub** verfolgt und versioniert werden.
- Eine **README-Datei** wird das Projekt beschreiben und Hinweise zur Installation und Nutzung geben.

### 3.8 Objektorientierung
- Das Programm soll unter Verwendung der **Objektorientierten Programmierung** umgesetzt werden. Klassen sollen verwendet werden, um die verschiedenen Aufgaben (z. B. Sensorsteuerung, Datenspeicherung) zu kapseln.

## 4. Nicht-funktionale Anforderungen

### 4.1 Benutzerfreundlichkeit
- Das User Interface muss einfach und intuitiv zu bedienen sein.

### 4.2 Skalierbarkeit
- Das System soll leicht erweiterbar sein, falls in Zukunft zusätzliche Sensoren oder Funktionen integriert werden sollen.

### 4.3 Zuverlässigkeit
- Das System muss zuverlässig und stabil laufen. Fehler beim Auslesen der Sensoren oder beim Senden der Daten an den Server müssen angemessen behandelt werden.

### 4.4 Leistung
- Die Aktualisierung der Messwerte soll in Echtzeit erfolgen, wobei eine Verzögerung von maximal 5 Sekunden toleriert wird.

## 5. Systemarchitektur

Das System besteht aus den folgenden Komponenten:

- **Mikrocontroller**: Raspberry Pi Pico W
- **Sensor**: BME280
- **Kommunikation**: HTTP-Requests (REST-API)
- **Datenbank**: Firebase (oder eine vergleichbare Lösung)
- **Web-Interface**: HTML
- **Entwicklungsumgebung**: Thonny, VS Code

## 6. Abnahmekriterien

- **Funktionstests**: Alle Messdaten müssen korrekt erfasst und übertragen werden.
- **Benutzer-Interface**: Das Interface muss korrekt die aktuellen Messwerte anzeigen.
- **Stabilität und Zuverlässigkeit**: Das System muss unter normalen Bedingungen zuverlässig laufen.

## 7. Anhang

Im Anhang wird die benötigte **Hardware** für den Mikrocontroller bereitgestellt.

- [BME280 Sensor]([https://www.adafruit.com/product/386](https://www.berrybase.de/gy-bme280-breakout-board-3in1-sensor-fuer-temperatur-luftfeuchtigkeit-und-luftdruck)
- [1.3" 128x64 OLED Display, SH1106, IIC/I2C Interface](https://www.berrybase.de/1.3-128x64-oled-display-sh1106-iic-i2c-interface-einfarbig-blau)
- [RGB LED SMD Modul](https://www.berrybase.de/rgb-led-smd-modul-mit-stiftleiste)

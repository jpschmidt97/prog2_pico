# Lastenheft: Indoor-Wetterstation (Raumluftmessung)

## 1. Ziel des Projekts

Das Ziel des Projekts ist die Entwicklung einer **Indoor-Wetterstation**, die in der Lage ist, grundlegende Raumluftparameter wie **Luftfeuchtigkeit**, **Temperatur** und **Luftdruck** zu erfassen. Diese Werte sollen auf einem **Mikrocontroller** wie dem **Raspberry Pi Pico W** erfasst und an einen **Server** übermittelt werden, wo die Daten langfristig gespeichert und visualisiert werden.

## 2. Projektumfang

- **Raumluftmessung**: Das Projekt umfasst die Erfassung und Messung von:
  - **Luftfeuchtigkeit**
  - **Temperatur**
  - **Luftdruck**
- **Lüftungsempfehlung**: Empfehlung zum Lüften basierend auf Luftfeuchtigkeit-Temperatur-Verhältnis soll optional mittels LED Ampel ausgegeben werden.
- **Mikrocontroller**: Das Projekt muss mit einem **Mikrocontroller** (z. B. **Raspberry Pi Pico W**) umgesetzt werden, der die Messungen durchführt und die Daten weiterverarbeitet.
- **Multitasking**: Es muss eine **einfaches Multitasking**-Konzept umgesetzt werden, sodass der Mikrocontroller **mehrere Aufgaben gleichzeitig** ausführen kann (z. B. Sensor auslesen, Daten senden, UI aktualisieren).
- **Kommunikation**: Der Mikrocontroller muss mit einem **Server** oder **Benutzer-Interface** kommunizieren können:
  - **Daten in beide Richtungen**: Der Mikrocontroller soll Daten senden und auch empfangen können (z. B. für Konfiguration).
- **Datenspeicherung**: Es muss eine **langfristige Datenspeicherung** umgesetzt werden, die über eine **Datenbank** (z. B. Firebase) realisiert wird.
- **Benutzer-Interface**: Ein **grafisches User-Interface** (GUI) muss in **HTML** entwickelt werden, das die gesammelten Daten anzeigt und dem Benutzer eine einfache Interaktion ermöglicht.
- **Qualitätssicherung**: Das Projekt muss gut dokumentiert werden, insbesondere durch die Verwendung von **Docstrings** im Code. Alle relevanten Dateien sollen im **GitHub-Repository** hochgeladen und versioniert werden.
- **Objektorientierung**: Das Mikrocontrollerprogramm muss unter Verwendung von **Objekten** und objektorientierten Prinzipien entwickelt werden.

## 3. Technische Anforderungen

- **Mikrocontroller**: Der Mikrocontroller muss ein **ESP8266** oder ein vergleichbarer Mikrocontroller sein, der über WiFi kommunizieren kann. In diesem Fall wird ein **Raspberry Pi Pico W** genutzt.
- **Sensoren**: Es müssen Sensoren für **Luftfeuchtigkeit**, **Temperatur** und **Luftdruck** verwendet werden (z. B. BME280).
- **Datenbank**: Es wird eine **Cloud-Datenbank** (z. B. Firebase) verwendet, um die Messdaten langfristig zu speichern.
- **Web-Interface**: Die Benutzeroberfläche wird als **HTML**-Seite realisiert. Das Interface muss die Messdaten in Echtzeit anzeigen und eine einfache Bedienung ermöglichen.
- **Kommunikation**: Der Mikrocontroller soll HTTP-Requests verwenden, um mit dem Server zu kommunizieren (z. B. über **REST-API**).
- **Multitasking**: Das Programm auf dem Mikrocontroller muss mehrere Aufgaben gleichzeitig ausführen können. Dafür werden **Interrupts** oder **Tasks** genutzt (je nach gewähltem Framework wie **ESPAsyncWebServer** oder **Arduino-Framework**).

## 4. Nicht-Ziele

- Keine mobile App oder externe Hardware, die nicht zum Kernprojekt gehört.
- Keine Verwendung von zu komplexen Kommunikationsprotokollen wie MQTT oder CoAP.
- Keine komplexe Alarm- oder Benachrichtigungsfunktionalität für den Benutzer.

## 5. Stakeholder

- **Projektleiter**: Mika Röder, Jean-Pascale Schmidt
- **Entwickler**: Mika Röder, Jean-Pascale Schmidt
- **Benutzer**: Personen, die das Gerät zur Überwachung der Raumluftqualität nutzen möchten (z. B. Smart-Home-Enthusiasten)
- **Auftraggeber**: Dozent (Prof. Matthias Kühnbach, Mika Röder, Jean-Pascale Schmidt)

## 6. Meilensteine

| Milestone                   | Beschreibung                                               | Fälligkeitsdatum |
|-----------------------------|------------------------------------------------------------|------------------|
| **Projektplan fertiggestellt**        | Definieren der Anforderungen und Auswählen der Hardware    | 18. April 2025     |
| **Hardwareaufbau**       | Auslesen von Sensordaten funktioniert, Verkabelung erfolgreich      | 15. Mai 2025     |
| **Kommunikation in alle Richtungen funktioniert** | WLAN-Verbindung und HTTP-Kommunikation einrichten und erfolgreich testen         | ??? 30. Mai 2025     |
| **GUI erstellt**      | Erste Version des HTML-UI mit Echtzeitdaten aus dem Mikrocontroller | ??? 10. Juni 2025    |
| **Datenspeicherung inkl. Datenbank**     | Implementierung der Datenbank und langfristige Speicherung | ??? 20. Juni 2025    |
| **Abschluss**            | Dokumentation und Code-Upload in GitHub                   | ??? 30. Juni 2025    |

## 7. Qualitätsanforderungen

- **Dokumentation**: Alle Funktionen des Codes müssen mit **Docstrings** dokumentiert werden. Das Projekt muss auf **GitHub** hochgeladen werden.
- **Benutzerfreundlichkeit**: Das User Interface soll einfach bedienbar und intuitiv sein, ohne umfangreiche Schulung.

## 8. Projektstruktur und Code-Organisation

- **Mikrocontrollercode**: Der Code wird in einer **objektorientierten Struktur** organisiert, wobei jede Sensor- und Kommunikationskomponente als eigenes Objekt behandelt wird. Die Programmierung erfolgt in Python (MicroPython).
- **Web-Server**: Ein einfaches Web-Interface wird auf dem **Raspberry Pi Pico W** eingerichtet, um die aktuellen Werte der Messsensoren an den Benutzer zu übertragen.
- **Datenbankzugriff**: Eine einfache **REST-API** wird erstellt, um die erfassten Daten an die **Cloud-Datenbank** zu übertragen.

## 9. Verwendete Technologien

- **Mikrocontroller**: Raspberry Pi Pico W
- **Sensoren**: BME280
- **Kommunikation**: HTTP-Requests (REST-API)
- **Datenbank**: Firebase (oder eine vergleichbare Lösung)
- **Web-Interface**: HTML
- **Entwicklungsumgebung**: Thonny, VS Code

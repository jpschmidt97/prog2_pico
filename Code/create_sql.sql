CREATE TABLE Messwerte (
    messwert_id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    temp REAL NOT NULL,
    press REAL NOT NULL,
    hum REAL NOT NULL
);

DELETE FROM Messwerte   #löscht alle Einträge, der pimary key bleibt aber weiter fortlaufend
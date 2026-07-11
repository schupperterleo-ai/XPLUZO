import sqlite3

# 1. Verbindung herstellen (Erstellt die Datei 'launcher.db' in deinem neuen Ordner)
verbindung = sqlite3.connect("launcher.db")
cursor = verbindung.cursor()

# 2. Tabelle für Cosmetics (dein Sakura Cape etc.) erstellen
cursor.execute("""
CREATE TABLE IF NOT EXISTS cosmetics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    preis INTEGER,
    dateiname TEXT
)
""")

# 3. Tabelle für Spieler (damit sich das System die Coins merkt) erstellen
cursor.execute("""
CREATE TABLE IF NOT EXISTS spieler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    minecraft_name TEXT,
    coins INTEGER DEFAULT 0
)
""")

# 4. Speichern und schließen
verbindung.commit()
verbindung.close()

print("✅ Erfolg! Die Datenbank 'launcher.db' wurde fehlerfrei erstellt!")

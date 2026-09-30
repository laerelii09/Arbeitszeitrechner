<div align="center">

# Arbeitszeit-Rechner

### Einfach. Schnell. Farbig.

Eine kleine Terminal-Anwendung zur Berechnung von Arbeitszeit, Pausen und Feierabend.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Lizenz](https://img.shields.io/badge/Lizenz-MIT-2ea44f?style=for-the-badge)](LICENSE)
[![Plattform](https://img.shields.io/badge/Plattform-Windows%20%7C%20Linux%20%7C%20macOS-6f42c1?style=for-the-badge)](https://www.python.org/)

[English](README.md) · [Deutsch](README_DE.md)

</div>

---

## Überblick

Der Arbeitszeit-Rechner ist eine schlanke Kommandozeilen-Anwendung in Python. Er beantwortet zwei Fragen aus dem Arbeitsalltag:

- **Wann ist heute Feierabend?**
- **Wie viel Netto-Arbeitszeit habe ich gearbeitet?**

Die Anwendung ist auf Deutsch und Englisch verfügbar und bietet sechs farbige Terminal-Themes. Sie benötigt keine externen Pakete und speichert keine Daten.

## Funktionen

- Feierabend aus Startzeit, Zielarbeitszeit und Pause berechnen.
- Netto-Arbeitszeit aus Startzeit, Endzeit und Pause berechnen.
- Zwischen sechs Terminal-Themes wählen.
- Deutsche oder englische Benutzeroberfläche verwenden.
- Ungültige Zeit-, Zahlen- und Menüeingaben erkennen und erneut abfragen.
- Unter Windows, Linux und macOS mit ANSI-fähigem Terminal ausführen.

## Voraussetzungen

- Python **3.8 oder neuer**
- Ein Terminal mit ANSI-Farbunterstützung
- Keine zusätzlichen Pakete

Die Anwendung verwendet ausschließlich die Python-Standardbibliothek, insbesondere `datetime`.

## Installation

Repository klonen und in den Projektordner wechseln:

```bash
git clone https://github.com/YOUR-USERNAME/Arbeitszeitrechner.git
cd Arbeitszeitrechner
```

Eine Paketinstallation ist nicht erforderlich.

## Anwendung starten

Deutsche Version starten:

```bash
python Deutsch/main.py
```

Englische Version starten:

```bash
python Englisch/main.py
```

Falls Python auf deinem System als `python3` verfügbar ist, verwende `python3` anstelle von `python`.

Die Befehle sollten aus dem Projekt-Hauptordner gestartet werden, damit die gemeinsame Datei `themes.py` korrekt importiert wird.

## Berechnungen

### Feierabend berechnen

Zuerst werden Startzeit und Pause in Minuten eingegeben. Danach wird eine der beiden fest eingebauten Zielarbeitszeiten gewählt:

1. **8 Stunden 24 Minuten**
2. **9 Stunden**

Die Berechnung lautet:

```text
Startzeit + Zielarbeitszeit + Pause = Feierabend
```

Beispiel:

```text
Startzeit:       08:00
Zielarbeitszeit: 8 Stunden 24 Minuten
Pause:           45 Minuten
Feierabend:      17:09
```

### Gearbeitete Zeit berechnen

Startzeit, Endzeit und Pause in Minuten eingeben. Daraus wird berechnet:

```text
(Endzeit - Startzeit) - Pause = Netto-Arbeitszeit
```

Beispiel:

```text
Startzeit:         08:00
Endzeit:           17:00
Pause:             45 Minuten
Netto-Arbeitszeit: 8 Stunden 15 Minuten
```

Die Zeiten werden am selben Tag interpretiert. Nachtschichten über Mitternacht, Datumsangaben und mehrere Pausen werden in der aktuellen Version nicht unterstützt. Ein Ergebnis unter null wird als ungültig abgelehnt.

## Themes

Die Theme-Definitionen liegen zentral in [themes.py](themes.py).

| Auswahl | Theme  |
| :-----: | :----- |
|    1    | Pink   |
|    2    | Türkis |
|    3    | Weiss  |
|    4    | Blau   |
|    5    | Grün   |
|    6    | Gelb   |

Bei einer unbekannten Auswahl wird automatisch das weisse Theme verwendet.

## Eingaben und Einschränkungen

- Zeiten müssen im 24-Stunden-Format `HH:MM` eingegeben werden, zum Beispiel `08:00` oder `17:30`.
- Pausen werden als ganze Minuten eingegeben.
- Die Zielarbeitszeit ist aktuell auf die beiden Menüoptionen beschränkt.
- Bei der Berechnung der gearbeiteten Zeit muss die Endzeit am selben Tag nach der Startzeit liegen.
- Ungültige Zeit-, Zahlen- und Menüeingaben können erneut eingegeben werden.

## Projektstruktur

```text
Arbeitszeitrechner/
├── README.md
├── README_DE.md
├── themes.py
├── LICENSE
├── .gitignore
├── Deutsch/
│   └── main.py
└── Englisch/
    └── main.py
```

| Datei              | Zweck                            |
| :----------------- | :------------------------------- |
| `README.md`        | Englische Dokumentation          |
| `README_DE.md`     | Deutsche Dokumentation           |
| `themes.py`        | Gemeinsame ANSI-Farbdefinitionen |
| `Deutsch/main.py`  | Deutsche Anwendung               |
| `Englisch/main.py` | Englische Anwendung              |
| `LICENSE`          | MIT-Lizenz                       |

## Optionaler globaler Befehl

Damit die Anwendung aus jedem Ordner gestartet werden kann, lässt sich ein globaler Shell-Befehl einrichten.

### Windows PowerShell

Diese Funktion zum PowerShell-Profil hinzufügen und den Pfad anpassen:

```powershell
function arbeitszeit {
    python "C:\Pfad\Zu\Arbeitszeitrechner\Deutsch\main.py"
}
```

Profil neu laden und Befehl ausführen:

```powershell
. $PROFILE
arbeitszeit
```

### Linux und macOS

Diesen Alias in `~/.bashrc` oder `~/.zshrc` eintragen:

```bash
alias arbeitszeit='python3 /pfad/zu/Arbeitszeitrechner/Deutsch/main.py'
```

Danach die Shell-Konfiguration mit `source ~/.bashrc` oder `source ~/.zshrc` neu laden.

## Lizenz

Dieses Projekt steht unter der [MIT-Lizenz](LICENSE).

## Autorin

**Lara**  
Informatikerin EFZ – Applikationsentwicklung  
Schweiz

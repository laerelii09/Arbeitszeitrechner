<div align="center">

# Arbeitszeit-Rechner

### Einfach. Schnell. Farbig.

Eine terminalbasierte Python-Anwendung zur Berechnung von Arbeitszeit, Pausen und Feierabend.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Lizenz](https://img.shields.io/badge/Lizenz-MIT-2ea44f?style=for-the-badge)](LICENSE)
[![Plattform](https://img.shields.io/badge/Plattform-Cross--Platform-6f42c1?style=for-the-badge)](https://www.python.org/)

[English](README.md) · [Deutsch](README_DE.md)

</div>

---

## Überblick

**Arbeitszeit-Rechner** ist eine schlanke Python-Kommandozeilenanwendung, die tägliche Arbeitszeitberechnungen einfach und schnell macht.

Die Anwendung bietet zwei Hauptfunktionen:

| Funktion                       | Beschreibung                                                                         |
| :----------------------------- | :----------------------------------------------------------------------------------- |
| **Feierabend berechnen**       | Berechnet das Ende des Arbeitstages anhand von Startzeit, Pause und Zielarbeitszeit. |
| **Gearbeitete Zeit berechnen** | Berechnet die effektive Netto-Arbeitszeit anhand von Startzeit, Endzeit und Pause.   |

Die Anwendung läuft direkt im Terminal, unterstützt Deutsch und Englisch und speichert keine Daten.

---

## Wofür ist die Anwendung gedacht?

Der Rechner ist für Alltagssituationen gedacht, in denen du schnell wissen möchtest:

- Wann kann ich heute Feierabend machen?
- Wie viele Stunden habe ich tatsächlich gearbeitet?
- Wie lange war meine Pause?
- Wann endet mein Arbeitstag bei einer bestimmten Zielarbeitszeit?

Die Anwendung kann außerdem mit einem globalen Befehl wie `arbeitszeit` eingerichtet werden.

---

## Funktionen

- **Arbeitszeitberechnung**
  - Netto-Arbeitszeit aus Startzeit, Endzeit und Pause berechnen.

- **Feierabendberechnung**
  - Das genaue Ende des Arbeitstages aus Startzeit, Zielarbeitszeit und Pause berechnen.

- **6 individuelle Themes**
  - Zwischen sechs verschiedenen Terminal-Farbschemata wählen.

- **Zwei Sprachen**
  - Deutsche und englische Version sind enthalten.

- **Eingabevalidierung**
  - Ungültige Zeitformate, Zahlen und Menüauswahlen werden abgelehnt und erneut abgefragt.

- **Keine externen Abhängigkeiten**
  - Die Anwendung verwendet nur die Python-Standardbibliothek.

- **Plattformübergreifend**
  - Für Windows-, Linux- und macOS-Terminals mit ANSI-Farbunterstützung geeignet.

---

## Themes

Die Anwendung enthält sechs verschiedene Themes. Alle Theme-Definitionen sind zentral in [themes.py](themes.py) gespeichert.

### Englische Benutzeroberfläche

| Auswahl | Theme      | Farbstil                   |
| :-----: | :--------- | :------------------------- |
|   `1`   | **Weiss**  | Minimalistisch / Monochrom |
|   `2`   | **Türkis** | Cyan / Weiches Grau        |
|   `3`   | **Pink**   | Rose / Zartes Pink         |
|   `4`   | **Blau**   | Tiefes Ozeanblau           |
|   `5`   | **Grün**   | Matrix-Grün                |
|   `6`   | **Gelb**   | Warmes Gelb                |

### Deutsche Benutzeroberfläche

Die deutsche Anwendung verwendet dieselben sechs Theme-Definitionen, aber eine andere Reihenfolge im Menü:

| Auswahl | Theme      | Farbstil                   |
| :-----: | :--------- | :------------------------- |
|   `1`   | **Pink**   | Rosa                       |
|   `2`   | **Türkis** | Cyan / Türkis              |
|   `3`   | **Weiss**  | Minimalistisch / Monochrom |
|   `4`   | **Blau**   | Tiefes Ozeanblau           |
|   `5`   | **Grün**   | Matrix-Grün                |
|   `6`   | **Gelb**   | Warmes Gelb                |

Bei einer ungültigen Theme-Auswahl verwendet die Anwendung automatisch das **weisse Theme**.

---

## Sprachen

Die Anwendung ist in zwei Sprachen verfügbar.

| Sprache      | Datei                                  |
| :----------- | :------------------------------------- |
| **Deutsch**  | [`Deutsch/main.py`](Deutsch/main.py)   |
| **Englisch** | [`Englisch/main.py`](Englisch/main.py) |

Beide Versionen verwenden die zentrale Datei [`themes.py`](themes.py) und dieselbe Berechnungslogik.

---

## Voraussetzungen

- **Python 3.8 oder neuer**
- Ein Terminal oder eine Kommandozeile mit ANSI-Farbunterstützung
- Keine zusätzlichen Python-Pakete erforderlich

Die Anwendung verwendet unter anderem folgende Python-Standardbibliotheken:

```text
datetime
sys
os
```

---

## Installation

### 1. Repository klonen

```bash
git clone https://github.com/YOUR-USERNAME/Arbeitszeitrechner.git
```

### 2. In den Projektordner wechseln

```bash
cd Arbeitszeitrechner
```

Eine Paketinstallation ist nicht erforderlich.

---

## Anwendung starten

Starte die Befehle aus dem Projekt-Hauptordner, damit die gemeinsame Datei `themes.py` korrekt importiert werden kann.

### Deutsche Version

```bash
python Deutsch/main.py
```

Falls auf deinem System `python3` verwendet wird:

```bash
python3 Deutsch/main.py
```

### Englische Version

```bash
python Englisch/main.py
```

Oder:

```bash
python3 Englisch/main.py
```

---

## Anwendungsbeispiel

Nach dem Start wählst du ein Theme und eine der verfügbaren Berechnungen.

```text
ARBEITSZEIT-RECHNER

Wähle ein Design:
[1] Pink  [2] Türkis  [3] Weiss
[4] Blau  [5] Grün    [6] Gelb

Auswahl: 1

Was möchtest du tun?
[1] Feierabend berechnen
[2] Gearbeitete Zeit berechnen

Auswahl: 1

Startzeit (HH:MM): 08:00
Pause in Minuten: 45

[1] 8 Stunden 24 Minuten
[2] 9 Stunden

Zielarbeitszeit: 1

Feierabend: 17:09 Uhr
```

In diesem Beispiel bedeutet Auswahl `1` eine Zielarbeitszeit von **8 Stunden und 24 Minuten**. Zusammen mit der 45-minütigen Pause ergibt sich eine gesamte verstrichene Zeit von 9 Stunden und 9 Minuten.

---

## So funktionieren die Berechnungen

### 1. Feierabend berechnen

Das Ende des Arbeitstages wird wie folgt berechnet:

```text
Startzeit + Zielarbeitszeit + Pause = Feierabend
```

#### Beispiel

```text
Startzeit:       08:00
Zielarbeitszeit: 08:24
Pause:           00:45
--------------------------------
Feierabend:      17:09
```

### 2. Gearbeitete Zeit berechnen

Die effektive Arbeitszeit wird wie folgt berechnet:

```text
(Endzeit - Startzeit) - Pause = Netto-Arbeitszeit
```

#### Beispiel

```text
Startzeit:         08:00
Endzeit:           17:00
Pause:             00:45
--------------------------------
Netto-Arbeitszeit: 08:15
```

Die Zeiten werden am selben Tag interpretiert. Nachtschichten über Mitternacht, Datumsangaben und mehrere Pausen werden in der aktuellen Version nicht unterstützt. Ein Ergebnis unter null wird als ungültig abgelehnt.

---

## Eingaberegeln und Einschränkungen

- Zeiten müssen im 24-Stunden-Format `HH:MM` eingegeben werden, zum Beispiel `08:00` oder `17:30`.
- Pausen müssen als ganze Minuten eingegeben werden.
- Die Zielarbeitszeit ist aktuell auf 8 Stunden 24 Minuten oder 9 Stunden beschränkt.
- Bei der Berechnung der gearbeiteten Zeit muss die Endzeit am selben Tag nach der Startzeit liegen.
- Mehrere Pausen und eine automatische Pausenberechnung werden nicht unterstützt.
- Ungültige Zeit-, Zahlen- und Menüeingaben werden abgelehnt und können erneut eingegeben werden.

---

## Globaler Befehl

Die Anwendung kann als globaler Befehl eingerichtet werden, damit sie aus jedem Ordner gestartet werden kann.

Zum Beispiel:

```text
arbeitszeit
```

Dadurch muss nicht jedes Mal der vollständige Python-Befehl eingegeben werden.

---

### Windows PowerShell

#### 1. PowerShell-Profil öffnen

```powershell
notepad $PROFILE
```

Falls das Profil noch nicht existiert:

```powershell
New-Item -Path $PROFILE -Type File -Force
```

#### 2. Funktion hinzufügen

Ersetze den Pfad durch den tatsächlichen Speicherort deines Projekts:

```powershell
function arbeitszeit {
    python "C:\Pfad\Zu\Arbeitszeitrechner\Deutsch\main.py"
}
```

#### 3. PowerShell-Profil neu laden

```powershell
. $PROFILE
```

Danach kann die Anwendung aus jedem Ordner gestartet werden:

```powershell
arbeitszeit
```

---

### Linux / macOS

#### 1. Shell-Konfiguration öffnen

Für Zsh:

```bash
nano ~/.zshrc
```

Für Bash:

```bash
nano ~/.bashrc
```

#### 2. Alias hinzufügen

```bash
alias arbeitszeit='python3 /pfad/zu/Arbeitszeitrechner/Deutsch/main.py'
```

#### 3. Konfiguration neu laden

Für Zsh:

```bash
source ~/.zshrc
```

Für Bash:

```bash
source ~/.bashrc
```

Danach kann die Anwendung mit folgendem Befehl gestartet werden:

```bash
arbeitszeit
```

---

## Projektstruktur

```text
Arbeitszeitrechner/
│
├── README.md
├── README_DE.md
├── themes.py
├── .gitignore
├── LICENSE
│
├── Deutsch/
│   └── main.py
│
└── Englisch/
    └── main.py
```

### Dateiübersicht

| Datei              | Zweck                                     |
| :----------------- | :---------------------------------------- |
| `README.md`        | Englische Projektdokumentation            |
| `README_DE.md`     | Deutsche Projektdokumentation             |
| `themes.py`        | Zentrale Definition aller Terminal-Themes |
| `Deutsch/main.py`  | Deutsche Version der Anwendung            |
| `Englisch/main.py` | Englische Version der Anwendung           |
| `.gitignore`       | Von Git ausgeschlossene Dateien           |
| `LICENSE`          | MIT-Lizenz                                |

---

## Technologien

| Technologie           | Zweck                             |
| :-------------------- | :-------------------------------- |
| **Python 3**          | Programmiersprache                |
| **datetime**          | Zeitberechnung und Formatierung   |
| **ANSI Escape Codes** | Terminalfarben und Gestaltung     |
| **Git**               | Versionsverwaltung                |
| **GitHub**            | Repository- und Projektverwaltung |

---

## Design

Die Anwendung verwendet ANSI-Escape-Codes, um eine farbige Terminal-Oberfläche zu erzeugen.

Das Farbsystem ist von der Anwendungslogik getrennt und in [`themes.py`](themes.py) gespeichert. Dadurch können bestehende Themes geändert oder neue hinzugefügt werden, ohne die Hauptdateien anpassen zu müssen.

---

## Fehlerbehandlung

Die Anwendung validiert Benutzereingaben vor der Berechnung.

Beispiele für ungültige Eingaben:

```text
Ungültiges Zeitformat
Ungültige Zahl
Ungültige Menüauswahl
Ungültige Theme-Auswahl
```

Anstatt abzustürzen, fordert die Anwendung zur erneuten Eingabe eines gültigen Werts auf. Eine berechnete Netto-Arbeitszeit unter null wird ebenfalls als ungültig abgelehnt.

---

## Autorin

**Lara**

Informatikerin EFZ - Applikationsentwicklung

Schweiz

---

## Lizenz

Dieses Projekt steht unter der **MIT-Lizenz**.

Weitere Informationen findest du in der Datei [LICENSE](LICENSE).

---

<div align="center">

**Arbeitszeit-Rechner**

Mit Python entwickelt.

</div>

<div align="center">

# Working Time Calculator

### Simple. Fast. Colorful.

A small terminal application for calculating working time, breaks and the end of the working day.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-2ea44f?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-6f42c1?style=for-the-badge)](https://www.python.org/)

[English](README.md) · [Deutsch](README_DE.md)

</div>

---

## Overview

Working Time Calculator is a lightweight command-line application written in Python. It helps you answer two everyday questions:

- **When does my working day end?**
- **How much net working time did I complete?**

The application is available in English and German and uses six terminal color themes. It has no external dependencies and stores no data.

## Features

- Calculate the end of a working day from a start time, target working time and break.
- Calculate net working time from a start time, end time and break.
- Choose between six terminal themes.
- Use either the English or German interface.
- Validate time, number and menu input and request it again when invalid.
- Run on Windows, Linux and macOS terminals with ANSI color support.

## Requirements

- Python **3.8 or newer**
- A terminal with ANSI color support
- No additional packages

The application uses only Python's standard library, especially `datetime`.

## Installation

Clone the repository and enter its directory:

```bash
git clone https://github.com/YOUR-USERNAME/Arbeitszeitrechner.git
cd Arbeitszeitrechner
```

No package installation is required.

## Run the application

Run the English version:

```bash
python Englisch/main.py
```

Run the German version:

```bash
python Deutsch/main.py
```

On systems where Python is available as `python3`, use `python3` instead of `python`.

Start the commands from the project root so that the shared `themes.py` file can be imported correctly.

## How it works

### Calculate end time

Choose a start time, enter the break in minutes and select one of the two built-in target times:

1. **8 hours 24 minutes**
2. **9 hours**

The end time is calculated as follows:

```text
start time + target working time + break = end time
```

Example:

```text
Start time:           08:00
Target working time:  8 hours 24 minutes
Break:                45 minutes
End time:             17:09
```

### Calculate worked time

Enter the start time, end time and break in minutes. The application calculates:

```text
(end time - start time) - break = net working time
```

Example:

```text
Start time:        08:00
End time:          17:00
Break:             45 minutes
Net working time:  8 hours 15 minutes
```

Times are interpreted on the same day. Overnight shifts, dates and multiple breaks are not supported by the current version. A result below zero is rejected as invalid.

## Themes

The theme definitions are stored centrally in [themes.py](themes.py).

### English interface

| Option | Theme     |
| :----: | :-------- |
|   1    | White     |
|   2    | Turquoise |
|   3    | Pink      |
|   4    | Blue      |
|   5    | Green     |
|   6    | Yellow    |

### German interface

| Option | Theme     |
| :----: | :-------- |
|   1    | Pink      |
|   2    | Turquoise |
|   3    | White     |
|   4    | Blue      |
|   5    | Green     |
|   6    | Yellow    |

If an unknown theme option is entered, the application falls back to the white theme.

## Input and limitations

- Times must use the 24-hour format `HH:MM`, for example `08:00` or `17:30`.
- Breaks are entered as whole minutes.
- The target working time is currently limited to the two options shown in the menu.
- The worked-time calculation expects the end time to be later than the start time on the same day.
- Invalid time, number and menu entries are rejected and can be entered again.

## Project structure

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

| File               | Purpose                             |
| :----------------- | :---------------------------------- |
| `README.md`        | English documentation               |
| `README_DE.md`     | German documentation                |
| `themes.py`        | Shared ANSI color theme definitions |
| `Deutsch/main.py`  | German application                  |
| `Englisch/main.py` | English application                 |
| `LICENSE`          | MIT license                         |

## Optional global command

You can create a shell command to start the application from any directory.

### Windows PowerShell

Add this function to your PowerShell profile. Replace the path with the actual project location:

```powershell
function arbeitszeit {
    python "C:\Path\To\Arbeitszeitrechner\Englisch\main.py"
}
```

Reload the profile and run the command:

```powershell
. $PROFILE
arbeitszeit
```

### Linux and macOS

Add this alias to `~/.bashrc` or `~/.zshrc`:

```bash
alias arbeitszeit='python3 /path/to/Arbeitszeitrechner/Englisch/main.py'
```

Reload the shell configuration with `source ~/.bashrc` or `source ~/.zshrc`, depending on your shell.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

**Lara**<br>
Informatikerin EFZ - Applikationsentwicklung<br>
Switzerland

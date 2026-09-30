<div align="center">

# Working Time Calculator

### Simple. Fast. Colorful.

A terminal-based Python application for calculating working hours, breaks and the end of the working day.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-2ea44f?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Cross--Platform-6f42c1?style=for-the-badge)](https://github.com/)

[English](README.md) · [Deutsch](README_DE.md)

</div>

---

## Overview

**Working Time Calculator** is a lightweight Python CLI application designed to make daily working-time calculations simple and fast.

The application provides two main functions:

| Function                  | Description                                                                                    |
| :------------------------ | :--------------------------------------------------------------------------------------------- |
| **Calculate End Time**    | Calculates when your working day ends based on your start time, break and target working time. |
| **Calculate Worked Time** | Calculates your effective net working time based on start time, end time and break.            |

---

## What is it for?

The calculator is designed for everyday situations where you quickly want to know:

- When can I finish work today?
- How many hours did I actually work?
- How much break time did I take?
- What is my exact end time based on my target hours?

The application runs directly in the terminal and can also be configured with a global command such as `arbeitszeit`.

---

## Features

- **Working Time Calculation**
  - Calculate net worked hours from start time, end time and break.

- **End Time Calculation**
  - Calculate the exact end of the working day from start time, target hours and break.

- **6 Custom Themes**
  - Choose between six different terminal color schemes.

- **Two Languages**
  - English and German versions are included.

- **Input Validation**
  - Invalid time formats and numerical inputs are handled safely.

- **No External Dependencies**
  - The application only uses Python's standard library.

- **Cross-Platform**
  - Designed to work on Windows, Linux and macOS terminals with ANSI color support.

---

## Themes

The application includes six different color themes.

All theme definitions are stored centrally in `themes.py`.

| Option | Theme         | Color Style             |
| :----: | :------------ | :---------------------- |
|  `1`   | **White**     | Minimalist / Monochrome |
|  `2`   | **Turquoise** | Cyan / Soft Gray        |
|  `3`   | **Pink**      | Rose / Soft Pink        |
|  `4`   | **Blue**      | Deep Ocean Blue         |
|  `5`   | **Green**     | Matrix Green            |
|  `6`   | **Yellow**    | Warm Yellow             |

If an invalid theme is selected, the application automatically uses the **White** theme.

---

## Languages

The application is available in two languages.

| Language    | File               |
| :---------- | :----------------- |
| **English** | `Englisch/main.py` |
| **German**  | `Deutsch/main.py`  |

Both versions use the same central `themes.py` file.

---

## Requirements

- **Python 3.8 or newer**
- A terminal / command line with ANSI color support
- No additional Python packages required

The application uses Python's built-in libraries, including:

```text
datetime
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Arbeitszeitrechner.git
```

### 2. Navigate into the project

```bash
cd Arbeitszeitrechner
```

---

## Running the Application

### English Version

```bash
python Englisch/main.py
```

On systems where `python3` is required:

```bash
python3 Englisch/main.py
```

### German Version

```bash
python Deutsch/main.py
```

Or:

```bash
python3 Deutsch/main.py
```

---

## Usage Example

After starting the application, you can select a theme and choose between the available calculations.

```text
WORKING TIME CALCULATOR

Choose a design:
[1] White  [2] Turquoise  [3] Pink
[4] Blue   [5] Green      [6] Yellow

Choose: 3

What would you like to do?
[1] Calculate end time
[2] Calculate worked time

Choose: 1

Start time (HH:MM): 08:00
Break in minutes: 45

[1] 8 hours 24 minutes
[2] 9 hours

Target working time: 1

End time: 17:09
```

---

## Global Command

The application can be configured as a global command so that it can be started from any directory.

For example:

```text
arbeitszeit
```

instead of entering the complete Python command every time.

---

### Windows PowerShell

#### 1. Open your PowerShell profile

```powershell
notepad $PROFILE
```

If the profile does not exist yet:

```powershell
New-Item -Path $PROFILE -Type File -Force
```

#### 2. Add the following function

Replace the path with the actual location of your project:

```powershell
function arbeitszeit {
    python "C:\Path\To\Arbeitszeitrechner\Englisch\main.py"
}
```

#### 3. Reload the PowerShell profile

```powershell
. $PROFILE
```

You can now start the application from any directory:

```powershell
arbeitszeit
```

---

### Linux / macOS

#### 1. Open your shell configuration

For Zsh:

```bash
nano ~/.zshrc
```

For Bash:

```bash
nano ~/.bashrc
```

#### 2. Add the alias

```bash
alias arbeitszeit='python3 /path/to/Arbeitszeitrechner/Englisch/main.py'
```

#### 3. Reload the configuration

For Zsh:

```bash
source ~/.zshrc
```

For Bash:

```bash
source ~/.bashrc
```

You can now start the application with:

```bash
arbeitszeit
```

---

## Project Structure

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

### File Overview

| File               | Purpose                                   |
| :----------------- | :---------------------------------------- |
| `README.md`        | English project documentation             |
| `README_DE.md`     | German project documentation              |
| `themes.py`        | Central definition of all terminal themes |
| `Deutsch/main.py`  | German version of the application         |
| `Englisch/main.py` | English version of the application        |
| `.gitignore`       | Files excluded from Git                   |
| `LICENSE`          | MIT license                               |

---

## How the Calculation Works

### 1. End Time Calculation

The application calculates the end of the working day using:

```text
Start Time + Target Working Time + Break = End Time
```

#### Example

```text
Start:              08:00
Target:             08:24
Break:              00:45
--------------------------------
End Time:           17:09
```

---

### 2. Worked Time Calculation

The effective working time is calculated using:

```text
(End Time - Start Time) - Break = Net Worked Time
```

#### Example

```text
Start:              08:00
End:                17:00
Break:              00:45
--------------------------------
Net Worked Time:    08:15
```

---

## Technologies

| Technology            | Purpose                           |
| :-------------------- | :-------------------------------- |
| **Python 3**          | Main programming language         |
| **datetime**          | Time calculations and formatting  |
| **ANSI Escape Codes** | Terminal colors and styling       |
| **Git**               | Version control                   |
| **GitHub**            | Repository and project management |

---

## Design

The application uses ANSI escape codes to create a colorful terminal interface.

The color system is separated from the application logic and stored in:

```text
themes.py
```

This makes it easier to modify existing themes or add new ones without changing the main application code.

---

## Error Handling

The application validates user input before performing calculations.

Examples of invalid input include:

```text
Invalid time format
Invalid number
Invalid menu selection
Invalid theme selection
```

Instead of crashing, the application asks the user to enter a valid value.

---

## Author

**Lara**

Informatikerin EFZ – Applikationsentwicklung

Switzerland

---

## License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for more information.

---

<div align="center">

**Working Time Calculator**

Built with Python.

</div>

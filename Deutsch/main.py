import datetime

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from themes import PINK, TURQUOISE, WHITE, BLUE, GREEN, YELLOW

themes = {
    "1": WHITE,
    "2": TURQUOISE,
    "3": PINK,
    "4": BLUE,
    "5": GREEN,
    "6": YELLOW
}

print("Wähle ein Design:")
print("[1] Pink")
print("[2] Türkis")
print("[3] Weiss")
print("[4] Blau")
print("[5] Grün")
print("[6] Gelb")

wahl = input("▶ Auswahl: ")

C = themes.get(wahl, WHITE)


def print_banner():
    print(f"{C['MAIN']}╔══════════════════════════════════════════════════════╗{C['RESET']}")
    print(f"{C['MAIN']}║{C['RESET']}  {C['BOLD']}ARBEITSZEIT-RECHNER{C['RESET']}                  {C['MAIN']}║{C['RESET']}")
    print(f"{C['MAIN']}╚══════════════════════════════════════════════════════╝{C['RESET']}")


def eingabe_zeit(prompt):
    while True:
        try:
            return datetime.datetime.strptime(input(prompt), "%H:%M")
        except ValueError:
            print(f"{C['GRAY']}Bitte Zeit im Format HH:MM eingeben.{C['RESET']}")


def eingabe_zahl(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f"{C['GRAY']}Bitte eine Zahl eingeben.{C['RESET']}")


def feierabend():
    print(f"\n{C['BOLD']}--------- Feierabend berechnen --------{C['RESET']}\n")

    start = eingabe_zeit("▶ Startzeit (HH:MM): ")
    pause = eingabe_zahl("▶ Pause in Minuten: ")

    print("\n[1] 8 Stunden 24 Minuten")
    print("[2] 9 Stunden")

    while True:
        wahl = input("▶ Zielarbeitszeit: ")

        if wahl == "1":
            arbeitszeit = 8 * 60 + 24
            break
        elif wahl == "2":
            arbeitszeit = 9 * 60
            break
        else:
            print("Bitte 1 oder 2 wählen.")

    ende = start + datetime.timedelta(minutes=arbeitszeit + pause)

    print(f"\n{C['BOLD']}Feierabend: {ende.strftime('%H:%M')} Uhr{C['RESET']}\n")


def gearbeitete_zeit():
    print(f"\n{C['BOLD']}-------- Gearbeitete Zeit berechnen --------{C['RESET']}\n")

    start = eingabe_zeit("▶ Startzeit (HH:MM): ")
    ende = eingabe_zeit("▶ Endzeit (HH:MM): ")
    pause = eingabe_zahl("▶ Pause in Minuten: ")

    minuten = int((ende - start).total_seconds() / 60) - pause

    if minuten < 0:
        print("Die eingegebene Zeit ist ungültig.")
        return

    stunden = minuten // 60
    minuten = minuten % 60

    print(f"\n{C['BOLD']}Netto-Arbeitszeit: {stunden} Std. {minuten:02d} Min.{C['RESET']}\n")


def main():
    print_banner()

    print(f"\n{C['BOLD']}Was möchtest du tun?{C['RESET']}")
    print("[1] Feierabend berechnen")
    print("[2] Gearbeitete Zeit berechnen")

    while True:
        auswahl = input("\n▶ Auswahl: ")

        if auswahl == "1":
            feierabend()
            break
        elif auswahl == "2":
            gearbeitete_zeit()
            break
        else:
            print("Bitte 1 oder 2 wählen.")


main()
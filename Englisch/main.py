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


print("Choose a design:")
print("[1] White")
print("[2] Turquoise")
print("[3] Pink")
print("[4] Blue")
print("[5] Green")
print("[6] Yellow")

choice = input("▶ Choose: ")

C = themes.get(choice, WHITE)


def print_banner():
    print(f"{C['MAIN']}╔══════════════════════════════════════════════════════╗{C['RESET']}")
    print(f"{C['MAIN']}║{C['RESET']}  {C['BOLD']}WORKING TIME CALCULATOR{C['RESET']}               {C['MAIN']}║{C['RESET']}")
    print(f"{C['MAIN']}╚══════════════════════════════════════════════════════╝{C['RESET']}")


def input_time(prompt):
    while True:
        try:
            return datetime.datetime.strptime(input(prompt), "%H:%M")
        except ValueError:
            print(f"{C['GRAY']}Please enter the time in the format HH:MM.{C['RESET']}")


def input_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f"{C['GRAY']}Please enter a number.{C['RESET']}")


def calculate_end_time():
    print(f"\n{C['BOLD']}--------- Calculate end time ---------{C['RESET']}\n")

    start_time = input_time("▶ Start time (HH:MM): ")
    break_minutes = input_number("▶ Break in minutes: ")

    print("\n[1] 8 hours 24 minutes")
    print("[2] 9 hours")

    while True:
        choice = input("▶ Target working time: ")

        if choice == "1":
            target_minutes = 8 * 60 + 24
            break
        elif choice == "2":
            target_minutes = 9 * 60
            break
        else:
            print("Please choose 1 or 2.")

    end_time = start_time + datetime.timedelta(
        minutes=target_minutes + break_minutes
    )

    print(
        f"\n{C['BOLD']}End time: "
        f"{end_time.strftime('%H:%M')}{C['RESET']}\n"
    )


def calculate_worked_time():
    print(f"\n{C['BOLD']}-------- Calculate worked time --------{C['RESET']}\n")

    start_time = input_time("▶ Start time (HH:MM): ")
    end_time = input_time("▶ End time (HH:MM): ")
    break_minutes = input_number("▶ Break in minutes: ")

    worked_minutes = (
        int((end_time - start_time).total_seconds() / 60)
        - break_minutes
    )

    if worked_minutes < 0:
        print("The entered time is invalid.")
        return

    hours = worked_minutes // 60
    minutes = worked_minutes % 60

    print(
        f"\n{C['BOLD']}Net working time: "
        f"{hours} hours {minutes:02d} minutes.{C['RESET']}\n"
    )


def main():
    print_banner()

    print(f"\n{C['BOLD']}What would you like to do?{C['RESET']}")
    print("[1] Calculate end time")
    print("[2] Calculate worked time")

    while True:
        choice = input("\n▶ Choose: ")

        if choice == "1":
            calculate_end_time()
            break
        elif choice == "2":
            calculate_worked_time()
            break
        else:
            print("Please choose 1 or 2.")


main()

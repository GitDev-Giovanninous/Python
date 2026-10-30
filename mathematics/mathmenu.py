from . import standard, scientific, programmer, date
from history import chronology
from colorama import Fore, init

def main():

    init(autoreset=True)

    while True:

        print("""\n=== MATH ===
1. Standard Calculator
2. Scientific Calculator
3. Programmer Calculator
4. Date calculation
5. Open Chronology
6. Exit""")

        choice = input("> ")

        if choice == "1":

            standard.main()

        elif choice == "2":

            scientific.main()

        elif choice == "3":

            programmer.main()

        elif choice == "4":

            date.main()

        elif choice == "5":

            chronology.read()

        elif choice == "6":

            break

        else:

            print(Fore.RED + "\nError")
            
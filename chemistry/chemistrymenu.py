from . import periodictablesearch, molarmass, phcalculator
from colorama import Fore, init


def main():

    init(autoreset=True)

    while True:

        print("""\n=== CHEMISTRY MENU ===
1. Search Element
2. Molar Mass Calculator
3. Ph Calculator
4. Exit""")

        choice = input("> ")

        if choice == "1":

            periodictablesearch.main()

        elif choice == "2":

            molarmass.main()

        elif choice == "3":

            phcalculator.main()

        elif choice == "4":

            return

        else:

            print(Fore.RED + "Error")

            continue

import periodictable as p
from colorama import Fore, init
from . import chemistrymenu


def main():

    init(autoreset=True)

    while True:

        try:

            print("\nEnter the chemical formula of a compound: (write q to quit)")

            formula = input()

            if formula == "":

                print(Fore.RED + "\nError")

            elif formula == "q":

                chemistrymenu.main()

            else:

                result = p.formula(formula)

                print(f"\n{result.mass} g/mol")

        except Exception:

            print(Fore.RED + "Error")

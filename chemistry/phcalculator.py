import math as m
from colorama import Fore, init
from . import chemistrymenu

def main():

    init(autoreset=True)

    while True:

        try:

            print("\nEnter the hydrogen ion concentration (H+) in mol/L: \n" + f"{Fore.RED}All pH values ​​are valid for aqueous solutions at 25°C. \nPress q to quit")

            h = input()

            if h == "q":

                chemistrymenu.main()

                return

            if float(h) > 0:

                ph = -m.log10(float(h))

                if ph > 7:

                    print(f"\nPh: {ph:.2f}. It's a basic solution")

                elif ph < 7: 

                    print(f"\nPh: {ph:.2f}. It's an acid solution")

                elif ph == 7:

                    print(f"\nPh: {ph:.2f}. It's a neutral solution")

            else:

                print(Fore.RED + "Error")

                continue

        except ValueError:

            print(Fore.RED + "Error")

if __name__ == "__main__":

    main()
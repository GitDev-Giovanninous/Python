from history import chronology as c
from . import mathmenu
from colorama import Fore, init

def conversion(base):

    init(autoreset=True)

    while True:

        try:

            n = int(input("\nNumber: "), base)

            result = f"""\n
Decimal: {int(n)}
Hexadecimal: {hex(n)[2:]}
Octagonal: {oct(n)[2:]}
Binary: {bin(n)[2:]}"""

            print(result)

            c.save(result)

            return

        except ValueError:

            print(Fore.RED + "\nError")

            continue

def main():

    while True:

        print("""\nChoose between:
1. Decimal
2. Octagonal
3. Hexadecimal
4. Binary
5. Quit""")

        choice = input()

        match choice:

            case "1":

                conversion(10)

            case "2":

                conversion(8)

            case "3":

                conversion(16)

            case "4":

                conversion(2)

            case "5":

                mathmenu.main()
                return

            case _:

                print(Fore.RED + "\nError")

                continue

if __name__ == "__main__":

    main()
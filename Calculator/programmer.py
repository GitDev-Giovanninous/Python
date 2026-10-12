import chronology as c
import menu

def conversion(base):

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

            print("Error")

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

                menu.main()

            case _:

                print("Error")

                continue

if __name__ == "__main__":

    main()
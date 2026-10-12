import scientific_operations as s
import chronology
import menu

def main():

    operation = {
        "sin": s.sin,
        "cos": s.cos,
        "tan": s.tan,
        "arcsin": s.arcsin,
        "arccos": s.arccos,
        "arctan": s.arctan,
        "x^2": s.square,                                                                                                           
        "x^3": s.cube,
        "sqrt": s.sqrt,
        "3^sqrt": s.sqrt3,
        "10^x": s.pow10,
        "log": s.log,
        "ln": s.ln,
        "1/x": s.reciproco,
        "abs": s.absolute,
        "!": s.factorial,
        "e^x": s.e_pow_x
    }

    while True:

        print("""\n
[Menu]

[sin] [cos] [tan]
[arcsin] [arccos] [arctan]
[x^2] [x^3]
[sqrt] [3^sqrt] [10^x]
[log] [ln] [1/x]
[abs] [!] [e^x]
[MO] [M-] [MC]""")

        user_input = input("\n>").lower().strip()

        if user_input == "menu":

            menu.main()

            continue

        elif user_input == "mo":

            chronology.read()

            continue

        elif user_input == "m-":

            chronology.delete()

            continue

        elif user_input == "mc":

            chronology.delete_all()

            continue

        if user_input in operation:

            try:

                number = float(input("Number: "))

            except ValueError:

                print("Error, retry")

                continue

            result = operation[user_input](number)

            result2 = f"{user_input} {number} = {result}"

            print(result2)

            chronology.save(result2)

        else:

            print("Operation not found, retry")

            continue

if __name__ == "__main__":
    main()
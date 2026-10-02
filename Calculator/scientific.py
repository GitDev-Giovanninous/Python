import scientific_operations as s
import standard

def main():

    result = None

    while True:

        print("""\n
[Standard C.]

[sin] [cos] [tan]
[arcsin] [arccos] [arctan]
[x^2] [x^3]
[sqrt] [3^sqrt] [10^x]
[log] [ln] [1/x]
[abs] [!] [e^x]""")

        user_input = input("\n>").lower().strip()

        if user_input == "standard":

            standard.main()

        number = float(input("\nNumber: ").strip())

        if type(number) == float:

            match user_input:

                case "sin":

                    result = s.sin(number)

                    print(f"Sin {number} = {result}")

                    result = None

                case "cos":

                    result = s.cos(number)

                    print(f"Cos {number} = {result}")

                    result = None

                case "tan":

                    result = s.tan(number)

                    print(f"Tan {number} = {result}")

                    result = None

                case "arcsin":

                    result = s.arcsin(number)
                    print(f"arcsin {number} = {result}")

                    result = None

                case "arccos":

                    result = s.arccos(number)
                    print(f"arccos {number} = {result}")

                    result = None

                case "arctan":

                    result = s.arctan(number)
                    print(f"arctan {number} = {result}")

                    result = None

                case "x^2":

                    result = s.square(number)
                    print(f"{number}^2 = {result}")

                    result = None

                case "x^3":

                    result = s.cube(number)
                    print(f"{number}^3 = {result}")

                    result = None

                case "10^x":

                    result = s.pow10(number)
                    print(f"10^{number} = {result}")

                    result = None

                case "sqrt":

                    result = s.sqrt(number)
                    print(f"sqrt {number} = {result}")

                    result = None

                case "3^sqrt":

                    result = s.sqrt3(number)
                    print(f"3^sqrt {number} = {result}")

                    result = None

                case "log":

                    result = s.log(number)
                    print(f"log {number} = {result}")

                    result = None

                case "ln":

                    result = s.ln(number)
                    print(f"ln {number} = {result}")

                    result = None

                case "1/x":

                    result = s.reciproco(number)
                    print(f"1/{number} = {result}")

                    result = None

                case "abs":

                    result = s.absolute(number)
                    print(f"abs {number} = {result}")

                    result = None

                case "!":

                    result = s.factorial(int(number))
                    print(f"{number}! = {result}")

                    result = None

                case "e^x":

                    result = s.e_pow_x(number)
                    print(f"e^{number} = {result}")

                    result = None

                case _:

                    print("Error")

                    result = None

                    continue
if __name__ == "__main__":
    main()
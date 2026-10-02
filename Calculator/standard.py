import scientific

def main():

    operation = ""

    while True:

        print("""\n
[Scientific C.]

[7] [8] [9] [x]
[4] [5] [6] [:]
[1] [2] [3] [+]
[0] [(] [)] [-]
[=] [.]""")
        

        user_input = input("\n>").lower().strip()

        match user_input:

            case "1":
                operation += "1"
                print(operation)
            case "2":
                operation += "2"
                print(operation)
            case "3":
                operation += "3"
                print(operation)
            case "4":
                operation += "4"
                print(operation)
            case "5":
                operation += "5"
                print(operation)
            case "6":
                operation += "6"
                print(operation)
            case "7":
                operation += "7"
                print(operation)
            case "8":
                operation += "8"
                print(operation)
            case "9":
                operation += "9"
                print(operation)
            case "0":
                operation += "0"
                print(operation)
            case ".":
                operation += "."
                print(operation)
            case "(":
                operation += "("
                print(operation)
            case ")":
                operation += ")"
                print(operation)
            case "x":
                operation += "*"
                print(operation)
            case ":":
                operation += "/"
                print(operation)
            case "+":
                operation += "+"
                print(operation)
            case "-":
                operation += "-"
                print(operation)
            case "=":

                try:

                    result = eval(operation)

                    print(f"\n{operation} = {result}")

                    operation = ""

                except NameError:

                    print("\nError")

                    operation = ""

                except SyntaxError:

                    print("\nSyntax Error")

                    operation = ""

            case "scientific":

                scientific.main()

            case _:

                print("Error")

                operation = ""

                continue

if __name__ == "__main__":
    main()
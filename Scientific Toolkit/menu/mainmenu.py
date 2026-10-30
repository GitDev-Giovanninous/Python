from mathematics import mathmenu
from chemistry import chemistrymenu
from colorama import Fore, init

def main():

    init(autoreset=True)

    while True:

        print("""\n=== SCIENTIFIC TOOLKIT ===
1. Mathematics
2. Chemistry
3. Physics
4. Exit""")

        choice = input("> ")

        if choice == "1":

            mathmenu.main()

        elif choice == "2":

            chemistrymenu.main()

        elif choice == "3":

            print(Fore.RED + "Not available")

        elif choice == "4":

            return

        else:

            print(Fore.RED + "\nError")

            continue
import datetime as dt
from . import mathmenu
from colorama import Fore, init

def date_difference():

    init(autoreset=True)

    while True:

        d1 = dt.date.today()

        d2 = input("\nInsert a data (day/month/year) (press q for quit): ")

        if d2 == "q":

            mathmenu.main()

            return

        try:
    
            d2 = dt.date.strptime(d2, "%d/%m/%Y")

            if d2 < d1:

                print(Fore.RED + "\nError")

                continue

            diff = d2 - d1

            diff = diff.days

            print(f"\nfrom {d1} to {d2} there are {diff} days left")

            return

        except ValueError:

            print(Fore.RED + "Error")

            continue

def main():

    date_difference()

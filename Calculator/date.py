import datetime as dt
import menu as m

def date_difference():

    while True:

        d1 = dt.date.today()

        d2 = input("\nInsert a data (day/month/year) (press q for quit): ")

        if d2 == "q":

            m.main()

        try:
    
            d2 = dt.date.strptime(d2, "%d/%m/%Y")

            if d2 < d1:

                print("\nError")

                continue

            diff = d2 - d1

            diff = diff.days

            print(f"\nfrom {d1} to {d2} there are {diff} days left")

            return

        except ValueError:

            print("Error")

            continue

def main():

    date_difference()

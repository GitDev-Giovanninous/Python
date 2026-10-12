import scientific as s
import standard as st
import chronology as c
import date as d
import programmer as p

def main():

    while True:

        print("""===== MENU =====

1. Standard Calculator
2. Scientific Calculator
3. Programmer Calculator
4. Date calculation
5. Open Chronology
6. Exit""")

        choice = input("> ")

        match choice:

            case "1":

                st.main()

            case "2":

                s.main()

            case "3":

                p.main()

            case "4":

                d.main()

            case "5":

                c.read()

            case "6":

                break
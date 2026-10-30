import periodictable as p
import mendeleev as m
from . import chemistrymenu
from colorama import Fore, init

def searchelement(name):

    init(autoreset=True)

    element = None

    for e in p.elements:
        
        if e.name.lower() == name.lower():

            element = e

            break

    if element is None:

        print(Fore.RED + "Element not found!")

        return

    else:

        m_element = m.element(e.symbol)

        info = {

            "\nSymbol": element.symbol,
            "Name": element.name,
            "Atomic Number": element.number,
            "Atomic Mass": element.mass,
            "Density": element.density,
            "Melting Point": m_element.melting_point,
            "Boiling Point": m_element.boiling_point,
            "Electronic configuration": m_element.econf,
            "Electronegativity": m_element.en_pauling,
            "Group": m_element.group_id,
            "Period": m_element.period

        }

        print("=== ELEMENT INFO ===")

        for k, v in info.items():

            print(f"{k}: {v}")

def main():

    while True:

        print("\nEnter the name of a chemical element to display its properties. \nwrite q to quit.")

        element = input().lower().strip()

        if element == "q":

            chemistrymenu.main()
            
            return

        else:

            searchelement(element)

if __name__ == "__main__":

    main()
    
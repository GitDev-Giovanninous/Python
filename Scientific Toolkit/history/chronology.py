from sys import platform
import os
import subprocess as sb

p = platform

def save(operation):

    with open("chronology.txt", "a", encoding="UTF-8") as chronology:

        chronology.write(f"{operation}\n")

def read():

    if not os.path.exists("chronology.txt"):
        
        return "File not found"

    if p == "win32":
                
        os.startfile("chronology.txt")

    elif p == "darwin":

        sb.run(["open", "chronology.txt"])

    else:

        sb.run(["xdg-open", "chronology.txt"])

def delete():

    try:

        with open("chronology.txt", "r", encoding="UTF-8") as chronology:

            operation = chronology.readlines()

            operation.pop()

        with open("chronology.txt", "w", encoding="UTF-8") as chronology:

            chronology.writelines(operation)

    except FileNotFoundError:

        return "File not found"

    except IndexError:

        return "Empty file"

def delete_all():

    with open("chronology.txt", "w", encoding="UTF-8"):

        pass


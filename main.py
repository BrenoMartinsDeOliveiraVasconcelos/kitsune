import os
from userlib import format, software
import json


def main():
    # Get software info and print
    info = json.load(open("./kitsune.json"))
    print(f"KITSUNE PROJECT\nv{info['build']} - DEV: {info['dev']}")

    # Gets the current path
    path = os.getcwd()

    while True:
        # Get the files and prints
        files = os.listdir(path)
        format.s_print(files)

        # Gets user input, then gets the command and args
        cmd = software.command(input("> "))
        print(cmd)


if __name__ == '__main__':
    main()

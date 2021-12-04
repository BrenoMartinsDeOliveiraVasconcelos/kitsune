import os
from userlib import format


def main():
    # Gets the current path
    path = os.getcwd()

    while True:
        # Get the files and prints
        files = os.listdir(path)
        format.s_print(files)

        input("> ")


if __name__ == '__main__':
    main()

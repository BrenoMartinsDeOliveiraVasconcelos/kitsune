import os
from userlib import format, software
import json


def main():
    # Get software info and print
    info = json.load(open("./kitsune.json"))
    print(f"KITSUNE PROJECT\nv{info['build']} - DEV: {info['dev']}")

    # Gets the current current_path
    current_path = os.getcwd()

    while True:
        # If the current path is an empty string, current path is defined to "/"
        if current_path == "":
            current_path = "/"

        # Get the files and prints
        files = os.listdir(current_path)

        format.s_print(files)

        # Gets user input, then gets the command and args
        raw_cmd = software.command(input("> "))

        # Saving the commands and the args into different variables
        cmd, arr = raw_cmd[0], raw_cmd[1:]

        if cmd == "cd":
            cd_to = current_path+"/"+"".join(arr)
            # Checks if the current_path exists
            if os.path.exists(cd_to):
                # Check if it is a folder or not
                if os.path.isdir(cd_to):
                    # Then check if cd input is '..' or '.' or none.
                    check_cd = (cd_to.replace("\\", "/")).split("/")
                    if check_cd[-1] == "..":
                        # Delete the last path
                        del check_cd[-1]
                        del check_cd[-1]
                    elif check_cd[-1] == '.':
                        del check_cd[-1]

                    cd_to = "/".join(check_cd)
                    current_path = cd_to
                else:
                    print("\033[31mNot a directory!")
            else:
                print("\033[31mDoes not exist.")
        else:
            # If no command, it will check if input is a valid path
            if os.path.exists(" ".join(raw_cmd)):
                # Then check if it is a folder
                if os.path.isdir(" ".join(raw_cmd)):
                    # ... and cd to it.
                    current_path = " ".join(raw_cmd)


if __name__ == '__main__':
    main()

import os
from userlib import format, software
import json


def main():
    # Get software info and print
    info = json.load(open("./kitsune.json"))
    print(f"KITSUNE PROJECT\nv{info['build']} - DEV: {info['dev']}")

    # Gets the current current_path
    current_path = os.getcwd()

    # Variable to save old value of current_path
    old_path = ""

    # Pre-definition of files
    files = []

    while True:
        # If the current path is an empty string, current path is defined to "/"
        if current_path == "":
            current_path = "/"

        # Get the files and prints
        try:
            files = os.listdir(current_path)
        except PermissionError:
            # In case of no permission to do so, current_path is back upped
            current_path = old_path
            software.error(0)

        format.s_print(files)

        # Gets user input, then gets the command and args
        raw_cmd = software.command(input("> "))

        # Saving the commands and the args into different variables
        cmd, arr = raw_cmd[0], raw_cmd[1:]

        # Raw args
        raw_args = " ".join(arr)

        if cmd == "cd":
            old_path = current_path
            cd_to = current_path+"/"+raw_args
            # Checks if the cd target exists
            # Checking if is different from "/"
            if os.path.exists(cd_to) and raw_args != "/":
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
                    # Not a directory
                    software.error(1)
            else:
                # Doesn't exist only if the path is not real
                if os.path.exists(raw_args):
                    if os.path.isdir(raw_args):
                        old_path = current_path
                        current_path = raw_args
                else:
                    software.error(2)
        elif cmd == "mkdir":
            # Create a folder
            os.mkdir(f"{current_path}/{' '.join(arr)}")
        elif cmd == "clear":
            software.clear()
        else:
            # If there is no command, it will check if input is a valid path
            if os.path.exists(" ".join(raw_cmd)):
                # Then check if it is a folder
                if os.path.isdir(" ".join(raw_cmd)):
                    # ... and cd to it. (if not ".." or "."
                    if " ".join(raw_cmd) not in ["..", "."]:
                        old_path = current_path
                        current_path = " ".join(raw_cmd)
                else:
                    # Case the path is not a valid directory, error is given.
                    software.error(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        software.error(-1)

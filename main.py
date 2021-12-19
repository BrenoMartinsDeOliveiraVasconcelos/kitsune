import os
import shutil
from userlib import format, software
import json
from sys import argv as sys_args
import readline
import platform


readline.clear_history()


def main():
    # Get software info and print
    info = json.load(open("./kitsune.json"))

    # Gets the current current_path
    current_path = os.getcwd()
    if len(sys_args) > 1:
        if not " ".join(sys_args[1:]).startswith("--"):
            current_path = " ".join(sys_args[1:])

    # Variable to save old value of current_path
    old_path = ""

    # Pre-definition of files
    files = []

    while True:
        try:
            print(f"KITSUNE PROJECT\nv{info['build']} - DEV: {info['dev']}\n{platform.system()}")
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
            except FileNotFoundError:
                software.error(2)
                current_path = os.getcwd()

            format.s_print(files, current_path)

            # Gets user input, then gets the command and args
            user_input = input("> ")
            while user_input == "":
                user_input = input("INSERT A VALID INPUT: ")

            raw_cmd = software.command(user_input)

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
            elif cmd == "make":
                # string with the final path
                end_path = f"{current_path}/{' '.join(arr[1:])}"
                # Create a folder
                if arr[0] == "dir":
                    os.mkdir(end_path)
                # create a file
                elif arr[0] == "file":
                    open(end_path, "w+").close()
            elif cmd == "file":
                target = f"{current_path}/{arr[1]}"
                # write on a file
                if arr[0] == "write":
                    open(target, "w").write(" ".join(arr[2:]))
                # append
                elif arr[0] == "append":
                    open(target, "a").write(" ".join(arr[2:]))
                elif arr[0] == "read":
                    print("\n".join(open(target, "r").readlines()))
                    software.pause()
            elif cmd == "copy":
                # copy files and directories
                source = current_path+f"/{arr[0]}"
                target = " ".join(arr[1:])
                if target[0] != "/":
                    target = current_path+f"/{target}"
                if os.path.isdir(source):
                    shutil.copytree(source, target)
                else:
                    shutil.copy(source, target)
            elif cmd == "remove":
                target = raw_args
                if not target.startswith("/"):
                    target = current_path+"/"+raw_args
                if not os.path.isdir(target):
                    os.remove(target)
                else:
                    shutil.rmtree(target)
            elif cmd == "exit":
                exit()
            elif cmd == "path":
                # Show the current path
                print(f"Current path: {current_path}")
                software.pause()
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
        except PermissionError:
            software.error(0)
        except NotADirectoryError:
            software.error(1)
        except FileNotFoundError:
            software.error(2)
        except FileExistsError:
            software.error(3)
        except IsADirectoryError:
            software.error(4)
        except OSError:
            software.error(5)
        except IndexError:
            software.error(6)

        software.clear()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        software.error(-1)

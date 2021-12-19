from library.internals import mathplus
import os
import platform
import mimetypes


def s_print(array: list, path: str) -> None:
    """
    Prints the content of "array" in a pretty way (or not)
    :param array: List
    :param path: Path
    :return: None
    """
    index = 0

    # Prints each item of "array"
    for value in array:
        # Check the mimetype of the current value
        mime_type = mimetypes.guess_type(f"{path}/{value}")[0]
        # divide the mime type between two
        try:
            mime_main = mime_type.split("/")[0]
        except (TypeError, AttributeError):
            mime_main = ""
        if os.path.isdir(f"{path}/{value}"):
            mime_symbol = "+"
        elif mime_main == "text":
            mime_symbol = "t"
        elif mime_main == "image":
            mime_symbol = "i"
        elif mime_main == "audio":
            mime_symbol = "a"
        elif mime_main == "video":
            mime_symbol = "v"
        elif mime_main == "application":
            mime_symbol = "b"
        else:
            mime_symbol = "?"
        # if index is even then it will print at right of the terminal
        # end parameter is set as empty string, so it won't break line after printing
        if mathplus.iseven(index):
            print(f"\033[32m[{mime_symbol}] \033[33m{value:<20}\033[0m", end="")
            # In case index has the same value of len(array)-1, will be broken a line.
            if len(array)-1 == index:
                print("\n", end="")
        else:
            # Else, prints on the left.
            # After printing, line will be broken.
            print(f"\033[33m{value:>20}\033[32m [{mime_symbol}]\033[33m\033[0m", end="\n")

        index += 1


def pause() -> None:
    """
    Pause

    :return: None
    """
    input("\033[0mENTER to continue.")


def command(string: str) -> list:
    """
    Return a list containing the command and its args
    :param string: String
    :return: list
    """

    return string.split(" ")


def error(e_id: int) -> None:
    """
    Gives an error
    -1 - Aborted
    0 - Permission denied
    1 - Not a directory
    2 - Doesn't exist
    3 - Already exists
    4 - Is a directory
    5 - Invalid argument
    6 - Too few arguments
    7 - Invalid codification
    :param e_id: error code
    :return: Nothing but lines on the console
    """

    print(f"\033[31m", end="")

    if e_id == -1:
        print("Aborted.\033[0m")
    elif e_id == 0:
        print("Permission denied!")
    elif e_id == 1:
        print("Not a directory.")
    elif e_id == 2:
        print("Specified path doesn't exist!")
    elif e_id == 3:
        print("Already exists.")
    elif e_id == 4:
        print("Is a directory.")
    elif e_id == 5:
        print("Invalid argument")
    elif e_id == 6:
        print("Too few arguments.")
    elif e_id == 7:
        print("Invalid file codification.")

    # Pause the program to show the error if not eid -1.
    if e_id >= 0:
        pause()


def clear() -> None:
    """
    Clear the console
    :return: None
    """

    os.system("clear" if platform.system() != "Windows" else "cls")

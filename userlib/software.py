import os
import platform


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

    :param e_id: error code
    :return: Nothing but lines on the console
    """

    print(f"\033[31m", end="")

    if e_id == -1:
        print("Aborted.")
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

    # Pause the program to show the error if not eid -1.
    if e_id >= 0:
        pause()


def clear() -> None:
    """
    Clear the console
    :return: None
    """

    os.system("clear" if platform.system() != "Windows" else "cls")

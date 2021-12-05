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

    # Pause the program to show the error if not eid -1.
    if e_id >= 0:
        input("ENTER to continue")

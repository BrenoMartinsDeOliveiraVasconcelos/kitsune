from userlib.internals import mathplus
import mimetypes
import os


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
        mime_symbol = ""
        mime_type = mimetypes.guess_extension(f"{path}/{value}")
        if os.path.isdir(f"{path}/{value}"):
            mime_symbol = "+"
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

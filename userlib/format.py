from userlib.internals import mathplus


def s_print(array: list) -> None:
    """
    Prints the content of "array" in a pretty way (or not)

    :param array: List
    :return: None
    """
    index = 0

    # Prints each item of "array"
    for value in array:
        # if index is even then it will print at right of the terminal
        # end parameter is set as empty string so it won't break line after printing
        if mathplus.iseven(index):
            print(f"{value:<15}", end="")
        else:
            # Else, prints on the left.
            # After printing, line will be broken.
            print(f"{value:>15}", end="\n")

        index += 1

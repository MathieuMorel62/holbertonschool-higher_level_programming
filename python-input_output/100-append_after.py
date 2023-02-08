#!/usr/bin/python3
""" Function that inserts a line of text to a file """


def append_after(filename="", search_string="", new_string=""):
    """
    Function that inserts a line of text to a file,
    after each line containing a specific string.
    """
    with open(filename, mode="r") as file:
        content = file.readlines()

    with open(filename, mode="w") as file:
        for line in content:
            file.write(line)
            if search_string in line:
                file.write(new_string)

#!/usr/bin/python3
""" Write to a file """


def write_file(filename="", text=""):
    """ Returns number of lines in text file """
    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(text)

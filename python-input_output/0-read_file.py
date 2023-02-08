#!/usr/bin/python3
""" Read file """


def read_file(filename=""):
    """Reads a text file (utf8) and prints to stdout"""
    with open(filename, encoding="utf8") as f:
        print(f.read(), end="")

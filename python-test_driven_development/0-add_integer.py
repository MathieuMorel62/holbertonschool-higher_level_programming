#!/usr/bin/python3
"""  function that adds 2 integers. """


def add_integer(a, b=98):
    """ function that adds 2 integers. """
    if isinstance(a, (int, float)):
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)):
        b = int(b)
    else:
        raise TypeError("b must be an integer")
    return (a + b)

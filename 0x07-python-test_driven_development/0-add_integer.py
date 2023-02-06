#!/usr/bin/python3
""" Function that adds 2 integers. """


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an int.

    Parameters:
    a (int or float): first value to add
    b (int or float): second value to add, default value is 98

    Returns:
    int: the sum of a and b

    Raises:
    TypeError: if a or b is not an integer or float
    """
    if isinstance(a, (int, float)):
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)):
        b = int(b)
    else:
        raise TypeError("b must be an integer")
    return (a + b)

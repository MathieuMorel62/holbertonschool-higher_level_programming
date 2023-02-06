#!/usr/bin/python3
""" function that prints a square with the character #. """


def print_square(size):
    """
    Summary
        Prints a square made of # characters with a specified size.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If the `size` argument is not an integer.
        ValueError: If the `size` argument is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for row in range(size):
            print("#" * size)

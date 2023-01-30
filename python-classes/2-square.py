#!/usr/bin/python3
"""Class Square that defines a square by its size attribute."""


class Square:
    """Class Square that defines a square by its size attribute."""

    def __init__(self, size = 0):
        """Instantiate a square with optional size.
        
        Args:
        size (int): Size of the square. Defaults to 0.
        
        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

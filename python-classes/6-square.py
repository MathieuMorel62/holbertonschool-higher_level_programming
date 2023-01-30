#!/usr/bin/python3
""" Class Square that defines a square by its size attribute. """


class Square:
    """ Class Square that defines a square by its size attribute. """

    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiate a square with optional size.

        Args:
        size (int): Size of the square. Defaults to 0.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Retrieve the size of the square. """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
        value (int): Size of the square.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Property getter to retrieve position """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Property setter to set position
        Raise TypeError if value is not a tuple of 2 positive integers
        """
        if type(value) != tuple or len(value) != 2 or \
            type(value[0]) != int or type(value[1]) != int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Return the current square area of a square. """
        return self.__size ** 2

    def my_print(self):
        """ Prints in stdout the square with the character # """
        if self.__size == 0:
            print()

        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

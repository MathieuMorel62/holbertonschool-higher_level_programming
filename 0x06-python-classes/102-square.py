#!/usr/bin/python3
"""Compare 2 squares"""


class Square:
    """ Define a square by its size """
    def __init__(self, size=0):
        """ Initialize square with size """
        self.size = size

    @property
    def size(self):
        """ Get size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Property setter for size of square
        Raise TypeError if value is not a number
        Raise ValueError if value is less than 0
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Return the area of the square """
        return self.size ** 2

    def __eq__(self, other):
        """ Check if two squares are equal """
        return self.area() == other.area()

    def __ne__(self, other):
        """ Check if two squares are not equal """
        return self.area() != other.area()

    def __gt__(self, other):
        """ Check if one square is greater than the other """
        return self.area() > other.area()

    def __ge__(self, other):
        """ Check if one square is greater than or equal to the other """
        return self.area() >= other.area()

    def __lt__(self, other):
        """ Check if one square is less than the other """
        return self.area() < other.area()

    def __le__(self, other):
        """  Check if one square is less than or equal to the other """
        return self.area() <= other.area()

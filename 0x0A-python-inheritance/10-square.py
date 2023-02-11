#!/usr/bin/python3
""" defines a basic geometric shape. """
Rectangle = __import__('9-rectangle').Rectangle


class BaseGeometry:
    """ A class that defines a basic geometric shape. """
    def area(self):
        """Raise an exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value for name
        name: string, name to be used in exceptions
        value: int, value to be validated
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Square(Rectangle):
    """ Init class square """
    def __init__(self, size):
        """ Instenciation """
        self.__size = size
        BaseGeometry.integer_validator(self, "size", size)
        super().__init__(size, size)

    def area(self):
        """ IReturn of area """
        return self.__size ** 2

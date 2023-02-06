#!/usr/bin/python3
""" defines a basic geometric shape. """


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

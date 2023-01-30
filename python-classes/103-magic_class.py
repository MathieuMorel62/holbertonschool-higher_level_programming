#!/usr/bin/python3
""" Python class MagicClass """
import math


class MagicClass:
    """ Class representing a Circle with a given radius """
    __radius = None

    def __init__(self, radius=0):
        """
        Initialize the Circle with a given radius.
        Raise TypeError if the given radius is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ Return the area of the Circle """
        return pow(self.__radius, 2) * math.pi

    def circumference(self):
        """ Return the circumference of the Circle """
        return 2 * math.pi * self.__radius

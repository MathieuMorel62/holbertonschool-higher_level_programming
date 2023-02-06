#!/usr/bin/python3
""" defines a basic geometric shape. """


class BaseGeometry:
    """ A class that defines a basic geometric shape. """
    def area(self):
        """ Raise an exception with the message 'area() is not implemented'. """
        raise Exception("area() is not implemented")

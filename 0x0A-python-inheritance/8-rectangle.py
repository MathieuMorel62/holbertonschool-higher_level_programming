#!/usr/bin/python3
""" class Rectangle that inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeometry class """
    def __init__(self, width, height):
        """ Initialize the rectangle object """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

#!/usr/bin/python3
"""  Simple rectangle """


class Rectangle:
    """ Define a rectangle with the given width and height. """
    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle with the given width and height.
        :param width: the width of the rectangle
        :param height: the height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Get the width of the rectangle.
        :return: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.
        :param value: the new width of the rectangle
        :raises TypeError: if value is not an integer
        :raises ValueError: if value is negative
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.
        :return: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.
        :param value: the new height of the rectangle
        :raises TypeError: if value is not an integer
        :raises ValueError: if value is negative
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Calculate the area of the rectangle. """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculate the perimeter of the rectangle. """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

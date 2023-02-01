#!/usr/bin/python3
"""  Simple rectangle """


class Rectangle:
    """ Define a rectangle with the given width and height. """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle with the given width and height.
        :param width: the width of the rectangle
        :param height: the height of the rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Get the width of the rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of the rectangle. """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Get the height of the rectangle. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height of the rectangle. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Calculate the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculate the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """ String representation of the rectangle using the character '#' """
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            string = str(self.print_symbol) * self.width
            return '\n'.join(string for i in range(self.height))

    def __repr__(self):
        """
        Return a string representation of the rectangle that can be used to
            recreate a new instance of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Print a message when an instance of the rectangle is deleted. """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            rect_2

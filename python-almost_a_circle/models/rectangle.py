#!/usr/bin/python3
""" Rectangle class that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize the Rectangle """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """ Print the rectangle represented by # """
        for i in range(self.y):
            print()
        for row in range(self.height):
            print(" " * self.x + self.width * "#")

    def __str__(self):
        """ Return string representation of the Rectangle instance """
        s_id = self.id
        s_x = self.x
        s_y = self.y
        s_wid = self.__width
        s_hei = self.__height
        return f"[Rectangle] ({s_id}) {s_x}/{s_y} - {s_wid}/{s_hei}"

    def update(self, *args, **kwargs):
        """ Updates the rectangle instance attributes with the arguments """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Dictionary representation of a Rectangle """
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
            }

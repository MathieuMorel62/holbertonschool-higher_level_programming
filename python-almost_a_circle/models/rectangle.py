#!/usr/bin/python3
""" Rectangle class that inherits from Base """

from models.base import Base


class Rectangle(Base):
    """ Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize the Rectangle """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

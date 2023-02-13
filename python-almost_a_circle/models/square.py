#!/usr/bin/python3
""" Square class that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize the Square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns a string representation of the Square """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ Return the size of the Square """
        return self.width

    @size.setter
    def size(self, value):
        """ Set the size of the Square """
        self.width = value
        self.height = value

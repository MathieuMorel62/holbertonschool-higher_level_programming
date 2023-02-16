#!/usr/bin/python3
""" Square class that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize the Square """
        super().__init__(size, size, x, y, id)


    @property
    def size(self):
        """ Return the size of the Square """
        return self.width

    @size.setter
    def size(self, value):
        """ Set the size of the Square """
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns a string representation of the Square """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """ Updates the square instance attributes with the arguments """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Dictionary representation of a Square """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
            }

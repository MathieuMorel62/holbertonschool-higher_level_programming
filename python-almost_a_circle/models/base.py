#!/usr/bin/python3
""" Base class """


class Base:
    """ Class to manage id attribute in all future classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class

        Args:
            id (int): The id of the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

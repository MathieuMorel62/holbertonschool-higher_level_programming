#!/usr/bin/python3
""" Base class """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This method writes the JSON string representation
        of a list of objects to a file
        """
        list_dictionaries = []
        if list_objs:
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())
            else:
                with open(f"{cls.__name__}.json", mode="w") as json_file:
                    json_file.write(cls.to_json_string(list_dictionaries))

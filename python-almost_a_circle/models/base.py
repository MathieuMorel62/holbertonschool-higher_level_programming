#!/usr/bin/python3
""" Base class """
import json
import os


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
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This method writes the JSON string representation
        of a list of objects to a file
        """
        if list_objs is None or len(list_objs) == 0:
            with open(f"{cls.__name__}.json", mode="w") as json_file:
                json_file.write("[]")
        else:
            list_dictionaries = []
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())
            with open(f"{cls.__name__}.json", mode="w") as json_file:
                json_file.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes set """
        if cls.__name__ == "Rectangle":
            instance = cls(4, 2)
        else:
            instance = cls(4)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances from a json file """
        filename = f"{cls.__name__}.json"
        if os.path.isfile(filename) is False:
            return []
        list = []
        with open(filename, "r") as file:
            json_content = file.read()
        list_json = cls.from_json_string(json_content)
        for instance in list_json:
            list.append(cls.create(**instance))
        return list

#!/usr/bin/python3
""" Student to JSON """


class Student:
    """ Class Student that defines a student """
    def __init__(self, first_name, last_name, age):
        """ Initialize a Student instance """
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    my_dict[key] = value
            return my_dict

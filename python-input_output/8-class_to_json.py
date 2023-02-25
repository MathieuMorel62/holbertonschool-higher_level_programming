#!/usr/bin/python3
""" Class to JSON """


def class_to_json(obj):
    """
    Function that returns the dictionary description of a Class for JSON
    serialization of an object.
    """
    return obj.__dict__

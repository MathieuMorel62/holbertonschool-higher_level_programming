#!/usr/bin/python3
""" Low memory cost """


class LockedClass:
    """
    Use the __slots__ class attribute to only
    allow 'first_name' instance attribute
    """
    __slots__ = ['first_name']

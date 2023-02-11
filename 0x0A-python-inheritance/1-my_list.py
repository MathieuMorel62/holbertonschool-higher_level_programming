#!/usr/bin/python3
""" Class that inherits from the built-in list type. """


class MyList(list):
    """  Adds a instance method 'print_sorted' to sort and print the list. """
    def print_sorted(self):
        """ Prints the sorted list (ascending sort) """
        print(sorted(self))

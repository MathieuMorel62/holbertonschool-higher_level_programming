#!/usr/bin/python3


class MyInt(int):
    """ Contrary class of int """
    def __eq__(self, other):
        """ Override the == to return the opposite result """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ Override the != to return the opposite result """
        return int.__eq__(self, other)

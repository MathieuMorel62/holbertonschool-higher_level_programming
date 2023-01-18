#!/usr/bin/python3


def remove_char_at(str, n):

    if n >= 0:
        a = str[:n]
        b = str[n + 1:]
        str = a + b
    return str

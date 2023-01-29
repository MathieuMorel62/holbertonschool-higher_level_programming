#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as message:
        print("Exception: {}".format(message), file=sys.stderr)
        return None

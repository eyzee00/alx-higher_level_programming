#!/usr/bin/python3
"""Module: defines a class-checking function"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a given class
        Returns True or False accordingly
    """
    if type(obj) == a_class:
        return True
    return False

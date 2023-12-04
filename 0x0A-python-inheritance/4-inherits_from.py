#!/usr/bin/python3
"""Module: defines inherits_from function"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance or inherited instance of a class
        Returns True or False accordingly
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

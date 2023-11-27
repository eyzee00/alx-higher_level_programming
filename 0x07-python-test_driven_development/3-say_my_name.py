#!/usr/bin/pyhton3
"""Module defining say_my_name function"""


def say_my_name(first_name, last_name=""):
    """Prints "My name is" followed by first and last name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
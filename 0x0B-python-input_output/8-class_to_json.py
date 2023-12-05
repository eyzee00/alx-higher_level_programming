#!/usr/bin/python3
"""Module: defines a function that returns the JSON
representation of the given class"""


def class_to_json(obj):
    """Returns the JSON representation of an object (string)"""
    return obj.__dict__

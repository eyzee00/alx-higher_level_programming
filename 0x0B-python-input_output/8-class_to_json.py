#!/usr/bin/python3
"""Module: defines a function that returns the JSON
representation of the given class"""

import json


def class_to_json(obj):
    """Returns the JSON representation of a class"""
    return json.dumps(obj.__dict__)

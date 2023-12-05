#!/usr/bin/python3
"""Module: defines a function that returns an object
(Python data structure) from its JSON string"""

import json


def from_json_string(my_str):
    """Returns the JSON representation of an object (string)"""
    return json.loads(my_str)

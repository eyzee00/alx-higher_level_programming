#!/usr/bin/python3
"""Module: defines a function that writes a 
JSON representation of an object to a text file"""

import json


def save_to_json_file(my_obj, filename):
    """Writes a JSON representation of an object 
    to a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

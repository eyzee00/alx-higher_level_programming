#!/usr/bin/python3
"""Module: defines a function that loads a JSON
representation from a text file"""

import json


def load_from_json_file(filename):
    """Returns an object (Python data structure) represented
    by a JSON string"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)

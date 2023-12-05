#!/usr/bin/python3
"""Module: defines a script that adds all arguments
to a Python list, and then save them to a file"""

import sys

if __name__ == "__main__":
    save = __import__('5-save_to_json_file').save
    load = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save(items, "add_item.json")
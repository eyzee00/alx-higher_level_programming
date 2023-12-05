#!/usr/bin/python3
"""Module: defines a function that adds all arguments
to a Python list, and then save them to a file"""

load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file


def add_item(filename, my_list=[]):
    """Adds all arguments to a Python list, and
    then save them to a text file"""
    new_list = load(filename)
    new_list.extend(my_list)
    save(new_list, filename)
    return new_list

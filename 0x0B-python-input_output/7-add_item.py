#!/usr/bin/python3
"""Module: defines a script that adds all arguments
to a Python list, and then save them to a file"""

from sys import argv
import os
load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file


if __name__ == "__main__":
    if os.path.exists("add_item.json"):
        my_list = load("add_item.json")
    else:
        my_list = []
    for i in range(1, len(argv)):
        my_list.append(argv[i])
    save(my_list, "add_item.json")

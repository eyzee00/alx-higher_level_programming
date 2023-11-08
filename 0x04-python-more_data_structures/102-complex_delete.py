#!/usr/bin/python3
def complex_delete(a_dictionary, target):
    while target in a_dictionary.values():
        for key, value in a_dictionary.items():
            if value is target:
                del a_dictionary[key]
                break

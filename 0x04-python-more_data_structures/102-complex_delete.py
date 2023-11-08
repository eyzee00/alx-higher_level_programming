#!/usr/bin/python3
def complex_delete(a_dictionary, target):
    for key, value in a_dictionary:
        if value is target:
            del a_dictionary[key]

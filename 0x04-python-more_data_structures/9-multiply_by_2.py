#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = dict(a_dictionary)
    for key in b_dictionary:
        b_dictionary[key] *= 2
    return b_dictionary

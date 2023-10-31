#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    copy = ""
    for letter in str:
        if i != n:
            copy = copy + letter
        i += 1
    return copy

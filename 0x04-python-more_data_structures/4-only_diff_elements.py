#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = {elem for elem in set_1 if elem not in set_2}
    return set_3

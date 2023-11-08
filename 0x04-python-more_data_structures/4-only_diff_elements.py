#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_list = []
    [unique_list.append(i) for i in set_1 if elem not in set_2]
    [unique_list.append(i) for i in set_2 if elem not in set_1]
    return unique_list

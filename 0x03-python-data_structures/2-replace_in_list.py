#!/usr/bin/python3
def replace_in_list(mylist, idx, new_value):
    if idx < 0:
        return mylist
    elif idx >= len(mylist):
        return mylist
    else:
        mylist[idx] = new_value
        return mylist


if __name__ == "__main__":
    my_list = [1, 2, 3, 4]
    replace_in_list(my_list, 0, -54)
    replace_in_list(my_list, 2, -54)
    print(my_list)

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = list(my_list)
    if idx >= 0 and idx < len(copy):
        copy[idx] = element
    return copy


if __name__ == "__main__":
    mylist = [1, 2, 3, 4]
    copy = new_in_list(mylist, 3, -54)
    print(copy)
    print("-------------------")
    print(mylist)

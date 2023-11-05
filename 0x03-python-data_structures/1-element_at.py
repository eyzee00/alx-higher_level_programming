#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    else:
        return my_list[idx]


if __name__ == "__main__":
    mylist = [-1, 7, -120, 89]
    print(element_at(mylist, 2))
    print(element_at(mylist, -1))
    print(element_at(mylist, 78))

#!/usr/bin/python3
def max_integer(mylist=[]):
    if mylist is None:
        return None
    switch = False
    for integer in mylist:
        if not switch:
            switch = True
            maximum = integer
        else:
            if integer > maximum:
                maximum = integer
    return maximum


if __name__ == "__main__":
    my_list = [0, -2, 4, -5785, 2]
    print(max_integer(my_list))

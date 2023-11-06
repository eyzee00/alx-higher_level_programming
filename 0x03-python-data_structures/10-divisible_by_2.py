#!/usr/bin/python3
def divisible_by_2(mylist=[]):
    boolist = mylist[:]
    i = 0
    index = 0
    while index < len(mylist):
        if not mylist[i] % 2:
            boolist[i] = True
        else:
            boolist[i] = False
        i += 1
        index += 1
    return boolist

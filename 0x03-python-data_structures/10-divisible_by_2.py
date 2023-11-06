#!/usr/bin/python3
def divisible_by_2(mylist=[]):
    boolist = mylist[:]
    i = 0
    while i < len(mylist):
        if not mylist[i] % 2:
            boolist[i] = True
        else:
            boolist[i] = False
        i += 1
    return boolist

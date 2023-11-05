#!/usr/bin/python3
def print_list_integer(mylist=[]):
    for element in mylist:
        print("{:d}".format(element))
if __name__ == "__main__":
    mylist = [1, 2, 3, 4]
    print_list_integer(mylist)

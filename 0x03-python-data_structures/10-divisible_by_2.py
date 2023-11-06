#!/usr/bin/python3
def divisible_by_2(mylist=[]):
    if mylist == []:
        return []
    boolist = []
    for integer in mylist:
        if not integer % 2:
            boolist.append(True)
        else:
            boolist.append(False)
    return boolist


if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_result = divisible_by_2(my_list)

    i = 0
    while i < len(list_result):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
        i += 1

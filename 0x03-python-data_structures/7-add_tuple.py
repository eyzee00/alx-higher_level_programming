#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a < 2:
        if len_a == 0:
            subtuple_a = (0, 0)
        else:
            subtuple_a = (tuple_a[0], 0)
    else:
        subtuple_a = (tuple_a[0], tuple_a[1])
    if len_b < 2:
        if len_b == 0:
            subtuple_b = (0, 0)
        else:
            subtuple_b = (tuple_b[0], 0)
    else:
        subtuple_b = (tuple_b[0], tuple_b[1])
    subtuple0 = subtuple_a[0] + subtuple_b[0]
    subtuple1 = subtuple_a[1] + subtuple_b[1]
    subtuple = (subtuple0, subtuple1)
    return subtuple


if __name__ == "__main__":
    tuple1 = (1, 2, 3)
    tuple2 = (1, 2)
    lister = list(tuple2)
    del lister[0]
    tuple2 = tuple(lister)
    print(add_tuple(tuple1, tuple2))

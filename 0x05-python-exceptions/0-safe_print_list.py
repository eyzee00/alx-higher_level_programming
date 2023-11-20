#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        printed_elements = 0
        for x in range(x):
            print("{}".format(my_list[x]), end="")
            printed_elements += 1
    except IndexError:
        print("")
        return printed_elements
    print("")
    return printed_elements


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))

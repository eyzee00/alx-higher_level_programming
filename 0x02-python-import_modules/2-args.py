#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print("1: {:s}".format(argv[1]))
    else:
        print("{:d} arguments:".format(len(argv) - 1))
        i = 1
        while i < len(argv):
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1

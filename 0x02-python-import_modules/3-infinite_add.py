#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    theInfiniteSum = 0
    i = 1
    while i < len(argv):
        theInfiniteSum = theInfiniteSum + int(argv[i])
        i += 1
    print("{:d}".format(theInfiniteSum))

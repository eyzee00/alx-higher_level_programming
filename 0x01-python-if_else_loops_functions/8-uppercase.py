#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if 97 <= ord(letter) <= 122:
            letter = chr(letter - 32)
        print("{:s}".format(str(letter)), end="")
    print("")

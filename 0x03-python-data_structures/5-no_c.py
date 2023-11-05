#!/usr/bin/python3
def no_c(my_string):
    modded_string = ""
    for letter in my_string:
        if letter != 'C' and letter != 'c':
            modded_string = modded_string + letter
    return modded_string


if __name__ == "__main__":
    mystring = "cccccciiiiiiiCCC"
    newstring = no_c(mystring)
    print(newstring)

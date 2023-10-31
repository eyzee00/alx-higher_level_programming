#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * (-1)
    print("{:d}".format(number % 10), end="")
    return number % 10
print_last_digit(98)
print_last_digit(0)
print_last_digit(1444)

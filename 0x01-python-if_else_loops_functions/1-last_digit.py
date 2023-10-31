#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = (number * (-1)) % 10
else:
    last_digit = number % 10
string = f"Last digit of {number:d} is {last_digit:d} and"
if last_digit > 5:
    print(string, "is greater than 5")
elif last_digit == 0:
    print(string, "is 0")
else:
    print(string, "is less than 6 and not 0")

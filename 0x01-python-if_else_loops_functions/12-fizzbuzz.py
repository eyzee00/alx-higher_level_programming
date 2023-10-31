#!/usr/bin/python3
def fizzbuzz():
    wordList = ["Fizz", "Buzz", "FizzBuzz"]
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 != 0:
            print("{:s} ".format(wordList[0]), end="")
        elif number % 5 == 0 and number % 3 != 0:
            print("{:s} ".format(wordList[1]), end="")
        elif number % 5 == 0 and number % 3 == 0:
            print("{:s} ".format(wordList[2]), end="")
        else:
            print("{:d} ".format(number), end="")
    print("")

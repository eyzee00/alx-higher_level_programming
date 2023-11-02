#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    if len(argv) != 4:
        errString = "Usage: ./100-my_calculator.py <a> <operator> <b>"
        print(errString)
        exit(1)
    listOfOperators = ["+", "-", "*", "/"]
    if argv[2] not in listOfOperators:
        errString = "Unknown operator. Available operators: +, -, * and /"
        print(errString)
        exit(1)
    formatString = "{} {} {} = {}"
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] is listOfOperators[0]:
        print(formatString.format(a, argv[2], b, add(a, b)))
    elif argv[2] is listOfOperators[1]:
        print(formatString.format(a, argv[2], b, sub(a, b)))
    elif argv[2] is listOfOperators[2]:
        print(formatString.format(a, argv[2], b, mul(a, b)))
    else:
        print(formatString.format(a, argv[2], b, div(a, b)))

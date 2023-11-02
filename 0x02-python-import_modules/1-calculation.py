#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, div, mul, sub
    a = 10
    b = 5
    formatStringAdd = "{:d} + {:d} = {:d}"
    formatStringSub = "{:d} - {:d} = {:d}"
    formatStringMul = "{:d} * {:d} = {:d}"
    formatStringDiv = "{:d} / {:d} = {:d}"
    print(formatStringAdd.format(a, b, add(a, b)))
    print(formatStringSub.format(a, b, sub(a, b)))
    print(formatStringMul.format(a, b, mul(a, b)))
    print(formatStringDiv.format(a, b, div(a, b)))

#!/usr/bin/python3
def safe_print_division(a, b):
    div_result = 0
    try:
        div_result = a / b
    except ZeroDivisionError:
        div_result = None
    finally:
        print("Inside result: {}".format(div_result))
        return div_result


if __name__ == "__main__":
    a = 12
    b = 2
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

    a = 12
    b = 0
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

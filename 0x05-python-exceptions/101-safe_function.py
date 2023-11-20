#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        fct_return = fct(*args)
    except Exception as error:
        stderr.write("Exception: {}\n".format(error))
        return None
    return fct_return

#!/usr/bin/python3
"""Module: defines a class named Square"""


class Square:
    """Square: defines a square object"""
    def __init__(self, size):
        """__init__: constructs a square object"""
        self.__size = size
        """__size: private attribute"""


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)

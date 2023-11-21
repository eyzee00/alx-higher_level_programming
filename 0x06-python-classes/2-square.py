#!/usr/bin/python3
"""Module: Defines a Square class"""


class Square:
    """Square: defines a Square object"""
    def __init__(self, size=0):
        """__init__: constructs a Square object"""
        if isinstance(size, int) is False:
            raise TypeError
        elif size < 0:
            raise ValueError
        self.__size = size

    def area(self):
        """area: returns the area of a Square object"""
        return self.__size ** 2


if __name__ == "__main__":
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))

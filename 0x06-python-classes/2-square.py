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
        else:
            self.__size = size

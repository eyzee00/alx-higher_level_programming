#!/usr/bin/python3
"""Module: defines a class Square"""


class Square:
    """Square: defines a Square object"""
    def __init__(self, size=0):
        """__init__: constructs a square instance"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __ne__(self, second):
        """defines the != logical operator"""
        return self.area() != second.area()

    def __eq__(self, second):
        """defines the == logical operator"""
        return self.area() == second.area()

    def __lt__(self, second):
        """defines the < logical operator"""
        return self.area() < second.area()

    def __le__(self, second):
        """defines the <= logical operator"""
        return self.area() <= second.area()

    def __gt__(self, second):
        """defines the > logical operator"""
        return self.area() > second.area()

    def __ge__(self, second):
        """defines the >= logical operator"""
        return self.area() >= second.area()


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")

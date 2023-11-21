#!/usr/bin/python3
"""Module: defines a square class"""


class Square:
    """Square: defines a square object"""
    def __init__(self, size=0):
        """__init__: constructs a square instance"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area: returns the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """my_print: prints a square instance"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")

    @property
    def size(self):
        """returns the value of the __size private attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the private attribute __size to value if possible"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value


if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()

    print("-------------")

    my_square.size = 10
    my_square.my_print()

    print("-------------")

    my_square.size = 0
    my_square.my_print()

    print("-------------")

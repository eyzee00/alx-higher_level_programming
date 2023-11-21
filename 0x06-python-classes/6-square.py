#!/usr/bin/python3
"""Module: defines a square class"""
positionerr = "position must be a tuple of 2 positive integers"


class Square:
    """Square: defines a square object"""
    def __init__(self, size=0, position=(0, 0)):
        """__init__: constructs a square instance"""
        if type(position) is not tuple:
            raise TypeError(positionerr)
        elif len(position) != 2:
            raise TypeError(positionerr)
        clause1 = isinstance(position[0], int) and position[0] >= 0
        clause2 = isinstance(position[1], int) and position[1] >= 0
        if not clause1 or not clause2:
            raise TypeError(positionerr)
        else:
            self.__position = position

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area: returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """my_print: prints a square instance"""
        leading_space = " " * self.__position[0]
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(leading_space, end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")

    @property
    def size(self):
        """gets the value of __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of __size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """gets the value of __position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the value of __position"""
        if type(value) is not tuple:
            raise TypeError(positionerr)
        elif len(value) != 2:
            raise TypeError(positionerr)
        clause1 = isinstance(value[0], int) and value[0] >= 0
        clause2 = isinstance(value[1], int) and value[1] >= 0
        if not clause1 or not clause2:
            raise TypeError(positionerr)
        else:
            self.__position = value


if __name__ == "__main__":
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--------------")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--------------")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--------------")

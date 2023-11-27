#!/usr/bin/python3
"""Module: define a Rectangle class"""


class Rectangle:
    """Rectangle: defines a class object"""
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """__init__: constructs an object """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        number_of_instances += 1

    def area(self):
        """area: returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter: returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def my_print(self):
        """my_print: prints a square instance"""
        if self.__width == 0 or self.__height == 0:
            print("")
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    print("#", end="")
                print("")

    def __str__(self):
        """__str__: returns a string representation of the object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    print("#", end="")
                if i < self.__height - 1:
                    print("")
            return ""

    def __repr__(self):
        """__repr__: returns a string representation of the object"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """__del__: prints a message when an object is deleted"""
        print("Bye rectangle...")

    @property
    def width(self):
        """width: returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """width: sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height: returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """height: sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

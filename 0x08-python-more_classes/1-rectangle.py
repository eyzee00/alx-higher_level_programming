#!/usr/bin/python3
"""Module: define a Rectangle class"""


class Rectangle:
    """Rectangle: defines a class object"""
    def __init__(self, width=0, height=0):
        """__init__: constructs an object """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width: returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """width: sets the width of the rectangle"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if type(value) is not int:
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """height: returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """height: sets the height of the rectangle"""
        if value < 0:
            raise ValueError("height must be >= 0")
        if type(value) is not int:
            raise TypeError("height must be an integer")
        self.__height = value


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.width)
    print(my_rectangle.height)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.width)
    print(my_rectangle.height)

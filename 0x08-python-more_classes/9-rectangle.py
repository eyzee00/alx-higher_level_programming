#!/usr/bin/python3
"""Module: define a Rectangle class"""


class Rectangle:
    """Rectangle: defines a class object"""
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

    def area(self):
        """area: returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter: returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def bigger_or_equal(rect_1, rect_2):
        """bigger_or_equal: returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def square(cls, size=0):
        """square: returns a Rectangle instance with width==height==size"""
        square_result = cls(size, size)
        return square_result

    def my_print(self):
        """my_print: prints a square instance"""
        if self.__width == 0 or self.__height == 0:
            print("")
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    print(self.print_symbol, end="")
                print("")

    def __str__(self):
        """__str__: returns a string representation of the object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    print(self.print_symbol, end="")
                if i < self.__height - 1:
                    print("")
            return ""

    def __repr__(self):
        """__repr__: returns a string representation of the object"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """__del__: prints a message when an object is deleted"""
        Rectangle.number_of_instances -= 1
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


if __name__ == "__main__":
    my_rectangle_1 = Rectangle(8, 4)
    print(my_rectangle_1)
    print("--")
    my_rectangle_1.print_symbol = "&"
    print(my_rectangle_1)
    print("--")

    my_rectangle_2 = Rectangle(2, 1)
    print(my_rectangle_2)
    print("--")
    Rectangle.print_symbol = "C"
    print(my_rectangle_2)
    print("--")

    my_rectangle_3 = Rectangle(7, 3)
    print(my_rectangle_3)

    print("--")

    my_rectangle_3.print_symbol = ["C", "is", "fun!"]
    print(my_rectangle_3)

    print("--")

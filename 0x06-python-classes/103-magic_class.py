#!/usr/bin/python3
"""Module: Define a MagicClass"""
import math


class MagicClass:
    """MagicClass: defines a circle object"""
    def __init__(self, radius=0):
        """__init__: constructs a MagicClass instance"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """returns the area of the MagicClass instance"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """returns the circumference of the MagicClass instance"""
        return ((2 * math.pi) * self.__radius)

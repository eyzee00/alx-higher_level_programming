#!/usr/vbin/python3
"""Module: defines a Square class"""

from typing import Any
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.__height

    @size.setter
    def size(self, value):
        """size setter"""
        self.__width = value
        self.__height = value

    def __str__(self):
        """str method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

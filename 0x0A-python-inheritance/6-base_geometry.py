#!/usr/bin/python3
"""Module: further definition of BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

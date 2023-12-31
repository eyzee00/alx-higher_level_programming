#!/usr/bin/python3
"""Module: defines a further class that defines a student"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Constructor for the Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the JSON representation of the student"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

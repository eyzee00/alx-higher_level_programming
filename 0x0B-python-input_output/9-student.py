#!/usr/bin/python3
"""Module: defines a class that defines a student"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Constructor for the Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the JSON representation of the student"""
        return self.__dict__

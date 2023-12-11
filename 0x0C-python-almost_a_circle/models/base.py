#!/usr/bin/python3
"""Module: defines a base class for all models"""

import json
import csv


class Base:
    """Base: mother class for all models"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        empty_json = "[]"
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return empty_json
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        empty_json = "[]"
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write(empty_json)
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            placeholder = cls(1, 1)
        elif cls.__name__ == "Square":
            placeholder = cls(1)
        placeholder.update(**dictionary)
        return placeholder

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                list_dicts = cls.from_json_string(f.read())
                return [cls.create(**dict) for dict in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes to CSV"""
        empty_csv = "[]"
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as f:
            if list_objs is None or len(list_objs) == 0:
                f.write(empty_csv)
            else:
                if cls.__name__ == "Rectangle":
                    attr_names = ["id", "width", "height", "x", "y"]
                else:
                    attr_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=attr_names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes from CSV"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as f:
                if cls.__name__ == "Rectangle":
                    attr_names = ["id", "width", "height", "x", "y"]
                else:
                    attr_names = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(f, fieldnames=attr_names)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []


if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

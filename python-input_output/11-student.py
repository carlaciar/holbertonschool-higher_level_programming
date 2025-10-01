#!/usr/bin/python3
"""
This module defines a Student class.
"""


class Student:
    """
    Represents a student with a first name, last name, and age.
    - If attrs is a list of strings, only attribute names
    contained in this list must be retrieved.
    Otherwise, all attributes must be retrieved
    - replaces all attributes of the Student instance
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        result = {}
        if isinstance(attrs, list):
            for name in attrs:
                if name in self.__dict__:
                    result[name] = self.__dict__[name]
            return result

        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)

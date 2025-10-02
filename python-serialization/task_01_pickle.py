#!/usr/bin/env
"""
this module serializes and deserializes custom
Python objects using the pickle module
"""

import pickle


class CustomObject:
    """
    serializes and deserializes custom
    Python objects using the pickle module
    """

    def __init__(self, name="", age=0, is_student=False):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                loaded = pickle.load(f)
                return loaded
        except (FileNotFoundError, EOFError, pickle.UnpicklingError, OSError):
            return None

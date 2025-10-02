#!/usr/bin/env
"""
basic serialization module that adds the functionality to serialize
a Python dictionary to a JSON file and deserialize the JSON file
to recreate the Python Dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    with open(filename, "r") as f:
        loaded = json.load(f)
        return loaded

#!/usr/bin/python3
"""
Module that defines a function that creates an Object from a “JSON file"
"""

import json


def load_from_json_file(filename):
    """
    Module that defines a function that
    creates an Object from a JSON file
    """

    with open(filename, "r") as f:
        obj = json.load(f)
        return obj

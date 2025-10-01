#!/usr/bin/python3
"""
Module that defines a function of a
JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""

    json_string = json.dumps(my_obj)
    return json_string

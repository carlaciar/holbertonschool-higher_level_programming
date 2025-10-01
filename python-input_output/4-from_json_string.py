#!/usr/bin/python3
"""
Module that defines a function of an object (Python data structure)
represented by a JSON string
"""

import json


def from_json_string(my_str):
    """an object (Python data structure) represented by a JSON string"""

    data = json.loads(my_str)
    return data

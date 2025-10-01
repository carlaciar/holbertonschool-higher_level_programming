#!/usr/bin/python3
"""
This module defines the class_to_json function.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.
    """

    return obj.__dict__

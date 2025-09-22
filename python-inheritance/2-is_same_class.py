#!/usr/bin/python3
"""
This module defines a function to check if an object
is an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Return True if obj is exactly an instance of a_class;
    otherwise return False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is exactly an instance of a_class,
        False otherwise.
    """

    if isinstance(obj, a_class):
        return type(obj) is a_class
    else:
        return False

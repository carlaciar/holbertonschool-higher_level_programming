#!/usr/bin/python3
"""
This module defines a function to check if an object
is an instance or if the object is an instance of a 
class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class
    or an instance of a class that is inherited;
    otherwise return False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is exactly an instance of a_class or inherited,
        False otherwise.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False

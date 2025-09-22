#!/usr/bin/python3
"""
This module defines a function to check if the object is an instance
of a class that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a subclass of a_class;
    False if obj is an instance of a_class itself or not related.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a subclass of a_class,
        False otherwise.
    """

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False

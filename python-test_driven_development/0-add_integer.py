#!/usr/bin/python3
"""
This module defines add_integer(a, b=98) that adds two integers.
"""

def add_integer(a, b=98):
    """
    Add two numbers as integers.

    Args:
        a (int or float): first number
        b (int or float): second number (default 98)

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b is not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

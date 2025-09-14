#!/usr/bin/python3
"""
This module defines add_integer(a, b=98) that adds two integers.
"""


def add_integer(a, b=98):
    """
    Add two numbers as integers.

    Args:
        a (int or float)
        b (int or float)

    Returns:
        int

    Raises:
        TypeError: if a or b is not int/float, or is non-finite (NaN/inf)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Convert with guard: map OverflowError/ValueError to TypeError
    try:
        a = int(a)
    except (OverflowError, ValueError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except (OverflowError, ValueError):
        raise TypeError("b must be an integer")

    return a + b

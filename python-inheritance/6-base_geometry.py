#!/usr/bin/python3
"""
This module defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    A base class that raises an Exception to indicate that
    area() is not implemented
    """

    def area(self):
        raise Exception("area() is not implemented")

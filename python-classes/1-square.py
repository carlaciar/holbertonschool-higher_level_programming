#!/usr/bin/python3
"""
This module defines a Square.
"""


class Square:
    """A class that will define a square.
    Private instance attribute: size
    Instantiation with size (no type/value verification)"""
    def __init__(self, size):
        self.__size = size

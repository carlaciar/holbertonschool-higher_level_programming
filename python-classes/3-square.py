#!/usr/bin/python3
"""
This module defines a Square.
"""


class Square:
    """A class that will define a square.
    Private instance attribute: size
    Instantiation with size (no type/value verification)"""
    def __init__(self, size=0):
        isinstance(size, int)
        self.__size = size

        if isinstance(size, int):
            pass
        else:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        self.area = int(self.__size) * int(self.__size)

        return self.area

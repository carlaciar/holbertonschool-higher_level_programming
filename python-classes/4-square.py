#!/usr/bin/python3
"""
This module defines a Square.
"""


class Square:
    """A class that will define a square.
    Private instance attribute: size
    Instantiation with size (no type/value verification)"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return int(self.__size) * int(self.__size)

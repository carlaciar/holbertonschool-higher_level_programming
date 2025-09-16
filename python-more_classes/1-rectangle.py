#!/usr/bin/python3
"""
This module defines an empty class Rectangle.
"""


class Rectangle:
    """An empty class that defines a rectangle."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            self.__width = value

        else:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            self.__height = value

        else:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

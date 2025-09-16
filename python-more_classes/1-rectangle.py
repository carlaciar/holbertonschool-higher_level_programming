#!/usr/bin/python3
"""
This module defines the Rectangle class.

The Rectangle class provides:
- A private instance attribute: width and height
- A property to retrieve width and height
- A setter to set width and height with type and value validation
- Instantiation with optional width and height (default is 0)
"""


class Rectangle:
    """Defines a square with a private width and height"""

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

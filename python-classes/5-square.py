#!/usr/bin/python3
"""
This module defines the Square class.

The Square class provides:
- A private instance attribute: size
- A property to retrieve size
- A setter to set size with type and value validation
- Instantiation with optional size (default is 0)
- A public method area() that returns the square area
"""


class Square:
    """Defines a square with a private size attribute and an area method."""
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

    def my_print(self):
        if self.__size == 0:
            print()

        else:
            for row in range(self.__size):
                print("#" * (self.__size))

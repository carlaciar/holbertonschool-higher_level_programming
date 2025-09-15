#!/usr/bin/python3
"""
This module defines the Square class.

The Square class provides:
- A private instance attribute: size and position
- A property to retrieve size and position
- A setter to set size and position with type and value validation
- Instantiation with optional size and position (default is 0)
- A public method area() that returns the square area
- A method to print # by the area
- A method to print # according to the position
"""


class Square:
    """
    Defines a square with a private size and position attribute
    and an area method.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            isinstance(value, tuple)
            and len(value) == 2
            and isinstance(value[0], int)
            and isinstance(value[1], int)
            and value[0] >= 0
            and value[1] >= 0
        ):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return int(self.__size) * int(self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for line in range(self.__position[1]):
            print()

        for row in range(self.__size):
            spaces = " " * self.__position[0]
            hash = "#" * self.__size
            print(spaces + hash)

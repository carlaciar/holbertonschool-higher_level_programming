#!/usr/bin/python3
"""
This module defines the Square class which is inherited from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    this class checks validates size by integer_validator
    gets the area of a square
    """

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size

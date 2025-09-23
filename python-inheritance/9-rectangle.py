#!/usr/bin/python3
"""
This module defines the Rectangle class which is inherited from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    this class checks validates width and height by integer_validator
    gets the area of a rectangle
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        self.area
        return self.__width * self.__height

    def __str__(self):
        rec = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return rec

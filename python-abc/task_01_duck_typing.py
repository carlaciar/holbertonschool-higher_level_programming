#!/usr/bin/env python3
"""
This file shows how to use classes for shapes.
There is a base Shape class, and two shapes: Circle and Rectangle.
Each shape can find its own area and perimeter.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    The base class for all shapes.
    Other shapes will inherit from this class.
    """
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    """
    A circle shape with a radius.
    Can calculate its area and perimeter (circumference).
    """
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius must be >= 0")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    A rectangle shape with a width and height.
    Can calculate its area and perimeter.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a given shape.
    The shape must have area() and perimeter() methods.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

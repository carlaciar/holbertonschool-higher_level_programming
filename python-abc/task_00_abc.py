#!/usr/bin/env python3
"""
This module defines an abstract Animal class and two concrete subclasses
(Dog and Cat).
Each subclass implements its own version of the sound() method.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class that represents an animal.
    Subclasses must implement the sound() method.
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    A Dog class that inherits from Animal.
    Implements the sound() method to return 'Bark'.
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    A Cat class that inherits from Animal.
    Implements the sound() method to return 'Meow'.
    """
    def sound(self):
        return "Meow"

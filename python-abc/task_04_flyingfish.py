#!/usr/bin/env python3
"""
Example of multiple inheritance with Fish, Bird, and FlyingFish classes.
"""

from abc import ABC, abstractmethod


class Fish(ABC):
    """A fish that can swim and lives in water."""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird(ABC):
    """A bird that can fly and lives in the sky."""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A flying fish that can both swim and fly,
    living in water and the sky.
    """

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


print(FlyingFish.mro())

#!/usr/bin/env python3
"""
A simple example of using mixins to add behaviors to a class.
"""


class SwimMixin:
    """Mixin that adds swimming ability."""
    def swim(self):
        """Print a swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying ability."""
    def fly(self):
        """Print a flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can swim, fly, and roar."""
    def roar(self):
        """Print a roaring action."""
        print("The dragon roars!")

#!/usr/bin/env python3
"""
A module that defines VerboseList, a subclass of UserList.
This class prints messages whenever the list is modified.
"""

from collections import UserList


class VerboseList(UserList):
    """A list that prints a message whenever it is modified."""

    def append(self, item):
        """Add an item to the list and print a message."""
        super().append(item)
        print("Added {} to the list.".format(item))

    def extend(self, items):
        """Extend the list and print how many items were added."""
        super().extend(items)
        print("Extended the list with {} items.".format(len(items)))

    def remove(self, item):
        """Remove an item from the list and print a message."""
        print("Removed {} from the list.".format(item))
        super().remove(item)

    def pop(self, i=-1):
        """Remove and return an item from the list and print a message."""
        item = super().pop(i)
        print("Popped {} from the list.".format(item))
        return item

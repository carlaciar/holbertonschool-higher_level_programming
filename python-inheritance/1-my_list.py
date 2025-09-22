#!/usr/bin/python3
"""
This module defines the MyList class.

The MyList class inherits from Python's built-in list
and adds a method to print the list in ascending order.
"""


class MyList(list):
    """
    A custom list class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))

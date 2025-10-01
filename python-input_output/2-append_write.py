#!/usr/bin/python3
"""
Module that defines a function to append a text file
and return the number of characters.
"""


def append_write(filename="", text=""):
    """Appends a text file (UTF8) and returns the number of characters"""

    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)
        return len(text)

#!/usr/bin/python3
"""
Module that defines a function to write a text file
and return the number of characters.
"""


def write_file(filename="", text=""):
    """Writes a text file (UTF8) and returns the number of characters"""

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
        return len(text)

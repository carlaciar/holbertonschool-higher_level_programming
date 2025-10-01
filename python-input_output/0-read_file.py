#!/usr/bin/python3
"""
Module that defines a function to read and print a text file (UTF8).
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints its contents to stdout."""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

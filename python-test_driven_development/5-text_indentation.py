#!/usr/bin/python3
"""
This module contains the function text_indentation
which prints text with two new lines after '.', '?', and ':'.
"""


def text_indentation(text):
    """Prints a text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): The text to format and print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        # print character
        print(text[i], end="")

        # if char is one of .,?,:
        if text[i] in ".?:":
            print("\n")
            # skip spaces after these characters
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

#!/usr/bin/python3
"""
This module defines a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            prev_row = triangle[-1]
            new_row = [1]
            for j in range(1, len(prev_row)):
                new_row.append(prev_row[j - 1] + prev_row[j])
            new_row.append(1)
            triangle.append(new_row)

    return triangle

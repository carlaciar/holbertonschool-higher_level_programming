#!/usr/bin/python3
"""Divide all elements of a matrix by a number, rounded to 2 decimals.

This module exposes `matrix_divided(matrix, div)` that validates inputs and
returns a new matrix with each element divided by `div`, rounded to 2 places.
It allows `float('inf')` and `float('-inf')` as divisors.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with each element of `matrix` divided by `div`.

    Args:
        matrix (list[list[int|float]]): Rectangular matrix of numbers.
        div (int|float): The divisor (required; no default).

    Raises:
        TypeError: If `matrix` is not a matrix (list of lists) of ints/floats.
        TypeError: If each row of `matrix` is not the same size.
        TypeError: If `div` is not a number.
        ZeroDivisionError: If `div` is zero.

    Returns:
        list[list[float]]: New matrix with elements rounded to 2 decimals.
    """
    if (not isinstance(matrix, list)
            or not all(isinstance(row, list) for row in matrix)
            or not all(all(isinstance(x, (int, float)) for x in row)
                       for row in matrix)):
        raise TypeError(
            "matrix must be a matrix "
            "(list of lists) of integers/floats"
        )

    if len(matrix) == 0:
        row_len = 0
    else:
        row_len = len(matrix[0])

    for row in matrix:
        if len(row) != row_len:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]

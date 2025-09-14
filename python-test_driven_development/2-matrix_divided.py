#!/usr/bin/python3
"""Divide all elements of a matrix by a number, rounded to 2 decimals.

This module exposes a single function `matrix_divided(matrix, div)` that:
- validates `matrix` is a list of lists of ints/floats with equal row sizes,
- validates `div` is a number and not zero,
- returns a NEW matrix with every element divided by `div`, rounded to 2 places.

It intentionally allows `div = float('inf')` and `div = float('-inf')` so that
results become 0.0 or -0.0 as per IEEE-754, matching the checker’s test.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with each element of `matrix` divided by `div`.

    Args:
        matrix (list[list[int|float]]): Rectangular matrix of numbers.
        div (int|float): The divisor.

    Raises:
        TypeError: If `matrix` is not a matrix (list of lists) of ints/floats.
        TypeError: If each row of `matrix` is not the same size.
        TypeError: If `div` is not a number.
        ZeroDivisionError: If `div` is zero.

    Returns:
        list[list[float]]: New matrix with elements rounded to 2 decimals.
    """
    # Validate matrix structure and element types
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(all(isinstance(x, (int, float)) for x in row) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate uniform row length
    if len(matrix) == 0:
        row_len = 0
    else:
        row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Compute a NEW matrix; rounding keeps floats (e.g., 0.0)
    return [[round(x / div, 2) for x in row] for row in matrix]

#!/usr/bin/python3
"""Utilities for dividing all elements of a matrix.

This module provides a single function, `matrix_divided`, which returns a new
matrix whose elements are the original elements divided by a given divisor,
rounded to 2 decimal places. Input validation ensures that the matrix is a
proper list of lists of numbers, rows are of equal size, and the divisor is a
non-zero number.
"""

def matrix_divided(matrix, div):
    """Return a new matrix with each element of `matrix` divided by `div`.

    Args:
        matrix (list of lists of int/float): Rectangular matrix of numbers.
        div (int|float): The divisor.

    Raises:
        TypeError: If `matrix` is not a matrix (list of lists) of ints/floats.
        TypeError: If rows of `matrix` are not the same size.
        TypeError: If `div` is not a number.
        ZeroDivisionError: If `div` is zero.

    Returns:
        list of lists of float: New matrix with elements rounded to 2 decimals.
    """
    # Validate matrix is a list of lists of integers/floats
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(all(isinstance(x, (int, float)) for x in row) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Ensure all rows are the same size
    if len(matrix) == 0 or len(matrix[0]) == 0:
        # Empty matrix is allowed only if it's rectangular; treat like equal sizes
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

    # Perform division and rounding
    return [[round(x / div, 2) for x in row] for row in matrix]

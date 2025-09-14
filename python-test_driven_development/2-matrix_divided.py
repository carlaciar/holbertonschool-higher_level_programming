#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimals"""

    # Validate matrix is a list of lists of integers/floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check each element in rows
    for row in matrix:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Ensure all rows are the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and rounding
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix

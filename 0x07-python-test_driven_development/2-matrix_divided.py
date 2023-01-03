#!/usr/bin/python3
"""
This module contains a function matrix_divided(matrix, div)
which divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Divide all elements

    Args:
        matrix (list): A list of lists of integer or floats
        div (int or float): The divisor
    Raises:
        TypeError: if the matrix has non numbers
        TypeError: if matrix contains rows of different sizes
        TypeError: if div is not an int or float
        ZeroDivisionError: if div is 0
    Returns:
        A new matrix of the division result
        """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])

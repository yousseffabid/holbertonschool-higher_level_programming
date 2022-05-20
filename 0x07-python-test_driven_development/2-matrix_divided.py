#!/usr/bin/python3

"""divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """divides all elements of matrix
    """
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (float, int)):
                raise TypeError("matrix must be a matrix\
                                (list of lists) of integers/floats")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = []
    for row in matrix:
        new.append(list(map(lambda x: round(x / div, 2), row)))
    return new

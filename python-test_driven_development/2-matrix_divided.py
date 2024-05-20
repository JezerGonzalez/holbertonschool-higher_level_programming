#!/usr/bin/python3
"""
This is a method for dividing a list of a list
"""


def matrix_divided(matrix, div):
    """
    Validates both lists are integers or floats to then divide them
    """

    matrix_err = "matrix must be a matrix (list of lists) of integers/floats"
    size_error = "Each row of the matrix must have the same size"
    result = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("div cannot be 0")
    for list in matrix:
        if len(list) != len(matrix[0]):
            raise TypeError(size_error)
        result_list = []
        for elements in list:
            if not isinstance(elements, (int, float)):
                raise TypeError(matrix_err)
            else:
                result_list.append(round(elements / div, 2))
        result.append(result_list)

    return result

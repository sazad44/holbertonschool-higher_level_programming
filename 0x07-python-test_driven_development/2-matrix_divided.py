#!/usr/bin/python3
"""Matrix Division module

This module divides a matrix by a number, checking for types and inputs.

"""


def matrix_divided(matrix, div):
    """matrix_divided function to divide matrix by div
    Return: matrix of results of each of original matrix's elements divided
    """
    try:
        return [[round(j/div, 2) for j in matrix[i]] for i in matrix]
    except TypeError:
        if not isinstance
        if not isinstance(matrix[i][j], int):
            message = 'matrix must be a matrix (list of lists) of\
            integers/floats'
            raise TypeError(message)
        elif not isinstance(matrix[i][j], float):
            message = 'matrix must be a matrix (list of lists) of\
            integers/floats'
            raise TypeError(message)

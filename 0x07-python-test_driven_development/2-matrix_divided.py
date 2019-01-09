#!/usr/bin/python3
"""Matrix Division module

This module divides a matrix by a number, checking for types and inputs.

"""


def matrix_divided(matrix, div):
    """matrix_divided function to divide matrix by div
    Return: matrix of results of each of original matrix's elements divided
    """
    try:
        if not isinstance(matrix, list):
            message = 'matrix must be a matrix (list of lists)\
 of integers/floats'
            raise TypeError(message)
        elif not isinstance(div, int) and not isinstance(div, float):
            raise TypeError('div must be a number')
        elif div == 0:
            raise ZeroDivisionError('division by zero')
        for i in matrix:
            if not isinstance(i, list):
                raise TypeError('matrix must be a matrix (list of lists) of\
 integers/floats')
            elif len(i) != len(matrix[0]):
                raise TypeError('Each row of the matrix must have the same\
 size')
        for i in range(len(matrix)):
            for j in matrix[i]:
                if isinstance(j, int) or isinstance(j, float):
                    round(float(j) / div, 2)
                else:
                    raise TypeError("""matrix must be a matrix (list of lists) \
of integers/floats""")
    except ValueError:
        if len(i) != len(matrix[0]):
                raise TypeError('Each row of the matrix must have the same\
 size')
        message = 'matrix must be a matrix (list of lists) of integers/floats'
        raise TypeError(message)

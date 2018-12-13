#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if isinstance(matrix, list):
        new_matrix = [[row[j]**2 for j in range(len(row))] for row in matrix]
        return new_matrix

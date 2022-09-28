#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for m in matrix:
        new_matrix.append(list(map(lambda x: x ** 2, m)))

    return new_matrix

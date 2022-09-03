#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[], [], []]
    for i in range(3):
        for column in matrix[i]:
            new_matrix[i].append(column**2)
    return new_matrix

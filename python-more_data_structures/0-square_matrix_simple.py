#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    for i in matrix:
        res.append([])
        for j in i:
            res[-1].append(j * j)

    return res

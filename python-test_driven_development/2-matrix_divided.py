#!/usr/bin/python3
"""Divide all elements of a matrix."""


def matrix_divided(matrix, div):
    """Return a new matrix with each value divided by div."""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    size = None
    res = []

    for r in matrix:
        if not isinstance(r, list):
            raise TypeError(
                "matrix must be a matrix "
                "(list of lists) of integers/floats"
            )

        if size is None:
            size = len(r)
        elif len(r) != size:
            raise TypeError("Each row of the matrix must have the same size")

        nr = []
        for n in r:
            if not isinstance(n, (int, float)):
                raise TypeError(
                    "matrix must be a matrix "
                    "(list of lists) of integers/floats"
                )
            nr.append(round(n / div, 2))
        res.append(nr)

    return res

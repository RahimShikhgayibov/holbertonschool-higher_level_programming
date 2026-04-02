#!/usr/bin/python3
"""Multiply 2 matrices."""


def matrix_mul(m_a, m_b):
    """Return the product of 2 matrices."""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if any(type(r) is not list for r in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(type(r) is not list for r in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for r in m_a:
        for n in r:
            if type(n) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")

    for r in m_b:
        for n in r:
            if type(n) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    w = len(m_a[0])
    for r in m_a:
        if len(r) != w:
            raise TypeError("each row of m_a must be of the same size")

    w = len(m_b[0])
    for r in m_b:
        if len(r) != w:
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            s = 0
            for k in range(len(m_b)):
                s += m_a[i][k] * m_b[k][j]
            row.append(s)
        res.append(row)

    return res

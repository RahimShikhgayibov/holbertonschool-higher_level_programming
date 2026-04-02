#!/usr/bin/python3
"""This module defines a function that adds two integers."""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: first number
        b: second number, which defaults to 98

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: if a or b is not an integer or float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)

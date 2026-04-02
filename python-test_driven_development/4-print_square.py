#!/usr/bin/python3
"""Print a square made of #."""


def print_square(size):
    """Print a square of size x size with #."""
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if type(size) not in [int]:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)

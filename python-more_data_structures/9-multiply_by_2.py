#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = {}
    for x, y in a_dictionary.items():
        res |= {x: y << 1}

    return res

#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    v = []
    for x, y in a_dictionary.items():
        if y == value:
            v.append(x)

    for x in v:
        a_dictionary.pop(x, None)

    return a_dictionary

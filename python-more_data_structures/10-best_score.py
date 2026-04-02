#!/usr/bin/python3
def best_score(a_dictionary):
    res, mx = None, None
    if a_dictionary is not None:
        for x, y in a_dictionary.items():
            if mx is None:
                res, mx = x, y
            elif mx < y:
                res, mx = x, y

    return res

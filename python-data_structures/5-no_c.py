#!/usr/bin/python3
def no_c(my_string):
    res = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            res += ch

    return res

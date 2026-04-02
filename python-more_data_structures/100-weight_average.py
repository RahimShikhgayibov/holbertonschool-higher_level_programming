#!/usr/bin/python3
def weight_average(my_list=[]):
    s, c = 0, 0
    for x, y in my_list:
        s += x * y
        c += y

    return 0 if c == 0 else s / c

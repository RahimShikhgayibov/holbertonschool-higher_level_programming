#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = []
    for i in my_list:
        res.append(False if i & 1 else True)

    return res

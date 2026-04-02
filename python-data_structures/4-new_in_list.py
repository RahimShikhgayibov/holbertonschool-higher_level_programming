#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx <= -1 or idx >= len(my_list):
        return my_list

    res = my_list.copy()
    res[idx] = element
    return res

#!/usr/bin/python3
def search_replace(my_list, search, replace):
    res = []
    for i in my_list:
        res.append(replace if i == search else i)

    return res

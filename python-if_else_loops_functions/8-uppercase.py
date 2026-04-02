#!/usr/bin/python3
def uppercase(str):
    if (len(str) == 0):
        print()
        return

    for i in range(len(str)):
        ch = chr(ord(str[i]) - (32 if 97 <= ord(str[i]) <= 122 else 0))
        print("{}".format(ch), end=("" if i != len(str) - 1 else "\n"))

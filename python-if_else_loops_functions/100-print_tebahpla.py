#!/usr/bin/python3
for i in range(58, 32, -1):
    ch = chr(i + (32 if i & 1 else 64))
    print("{}".format(ch), end='')

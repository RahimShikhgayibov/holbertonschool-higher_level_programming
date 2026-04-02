#!/usr/bin/python3
for i in range(0, 100):
    i1, i2 = i // 10, i % 10
    if i1 < i2:
        print("{}{}".format(i1, i2), end=(", " if i != 89 else "\n"))

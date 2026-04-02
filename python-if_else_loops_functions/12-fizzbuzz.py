#!/usr/bin/python3
def fizzbuzz():
    fizz, buzz, flag = 0, 0, 0
    for i in range(1, 101):
        flag = 0
        fizz += 1
        buzz += 1
        if fizz == 3:
            print("Fizz", end='')
            fizz, flag = 0, 1
        if buzz == 5:
            print("Buzz", end='')
            buzz, flag = 0, 1
        if flag == 0:
            print(i, end=' ')
        else:
            print(end=' ')

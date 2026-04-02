#!/usr/bin/python3
from sys import argv


def main():
    if len(argv) <= 1:
        print("0 arguments.")
        return

    ch = ('s' if len(argv) > 2 else '')
    print("{} argument{}:".format(len(argv) - 1, ch))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()

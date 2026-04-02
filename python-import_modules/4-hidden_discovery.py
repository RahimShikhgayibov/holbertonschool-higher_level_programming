#!/usr/bin/python3
import hidden_4


def main():
    for i in sorted(dir(hidden_4)):
        if not i.startswith("__"):
            print(i)


if __name__ == "__main__":
    main()

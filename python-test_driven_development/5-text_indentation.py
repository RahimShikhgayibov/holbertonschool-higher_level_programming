#!/usr/bin/python3
"""Print text with 2 new lines after ., ? and :."""


def text_indentation(text):
    """Print text with indentation after special characters."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = ""

    for c in text:
        s += c
        if c in ".?:":
            print(s.strip(), end="\n\n")
            s = ""

    print(s.strip(), end="")

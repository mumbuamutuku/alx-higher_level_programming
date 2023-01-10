#!/bin/usr/python3
"""Define a function which appends string at the end of a UTF8 text file"""


def append_write(filename="", text=""):
    """A function which appends text
    Args:
        filename: name of file
        text:  string to append
    """
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)

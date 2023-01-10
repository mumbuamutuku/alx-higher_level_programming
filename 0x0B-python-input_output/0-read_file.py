#!/usr/bin/python3
"""Define a read file from text file function."""


def read_file(filename=""):
    """Read from file function and print to stdout
    Args:
        filename - the file to read from
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

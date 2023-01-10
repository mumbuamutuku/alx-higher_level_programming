#!/usr/bin/python3
"""Define a function that wwrites a string to a UTF8 text file"""


def write_file(filename="", text=""):
    """A function which writes a string to a text file
    Args:
        filename: the file to write into
        text: contents to be written to the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3
"""
This module has one function: add_integer(a,b)
add_integer(a,b) : Return a + b
"""


def add_integer(a, b=98):
    """A function to add two integers
        Args:
            a, b int or float
            Return int(a) + int (b)
            """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an Integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

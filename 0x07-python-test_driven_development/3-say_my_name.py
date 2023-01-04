#!/usr/bin/python3
"""
This is the Name module
This module contains a simple function to print out a first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name (string)
        last_name (string)
    Raises:
        TypeError: if first_name and last_name are not strings

    Return nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

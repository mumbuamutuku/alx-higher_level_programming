#!/usr/bin/python3
"""Define a function that writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file
    using a JSON representation
    Args:
        filename: name of file to write
        my_obj: object to write
    """
    with open(filename, "w") as outfile:
        outfile.write(my_obj)

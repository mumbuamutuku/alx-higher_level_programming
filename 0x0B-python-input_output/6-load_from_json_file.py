#!/usr/bin/python3
"""Define a function that creates an Object from aJSON file"""
import json


def load_from_json_file(filename):
    """A function to create an objectt
    Args:
        filename: the name of file"""
    with open(filename, "r") as openfile:
        json_object = json.load(openfile)
    return json_object

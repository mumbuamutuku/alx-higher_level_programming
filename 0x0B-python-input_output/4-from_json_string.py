#!/usr/bin/python3
"""Define a function which returns an object represented by a Json string"""
import json


def from_json_string(my_str):
    """Return the python object representation of a JSON string."""
    return json.loads(my_str)

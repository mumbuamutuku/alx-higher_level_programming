#!/usr/bin/python3
"""Define a JSON representation function"""
import json


def to_json_string(my_obj):
    """A function which returns the JSON rep of an object"""
    return json.dumps(my_obj)

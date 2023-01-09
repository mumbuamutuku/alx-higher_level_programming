#!/usr/bin/python3
"""Define a class"""


class BaseGeometry:
    """public instance method area

    Raises:
        Exception with the message area() is not implemented"""
    def area(self):
        raise Exception("area() is not implemented")

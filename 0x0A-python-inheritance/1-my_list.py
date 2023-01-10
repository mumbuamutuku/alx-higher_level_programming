#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class Mylist(list):
    """Implements sorted printing for the built-in list class.
    it inherits from lst
    Returns:
        sorted list"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))

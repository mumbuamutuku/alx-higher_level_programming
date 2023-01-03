#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new Square

        Args:
            width
            height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the current width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set the current height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the current area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the current perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        if self.__width > 0 < self.__height:
            line = '#' * self.__width
            rectangle = (line + '\n') * (self.__height - 1) + line
        else:
            return ("")
        return (rectangle)

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))
        
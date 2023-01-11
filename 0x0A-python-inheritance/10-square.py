#!/usr/bin/python3
""" Class Square imports and inherits class Rectangle which inherits class BaseGeometry """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
	""" initiliaze class"""
	def __init__(self, size):
		""" Initialize function
		Args:
			size (int): size of square
		size should be validated
		"""
		super().integer_validator("size", size)
		super().__init__(size, size)
		self.__size = size


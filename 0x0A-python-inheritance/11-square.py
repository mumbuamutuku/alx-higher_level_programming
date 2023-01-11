#!/usr/bin/python3
""" Class Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
	"""Class Square inherits from class Rectangle"""
	def __init__(self, size):
		"""Class initialization
		Args:
			size (int): size of square
		"""
		super().integer_validator("size", size)
		super().__init__(size, size)
		self.__size = size

	def __str__(self):
		"""
		A DESCRIPTION OF THE SQUARE 
		"""
		return ("[Square] " + str(self.__size) + "/" + str(self.__size))


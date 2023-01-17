#!/usr/bin/python3
"""Documentation for Square class
Based on class Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class based on Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize instances"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """special string with
        square attributes"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """method that assigns attributes
        args is the list of arguments
        kwargs is the attribute dictionary
        """
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                    self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            if len(kwargs) > 0:
                keys = kwargs.keys()
                for i in keys:
                    if i == 'id':
                        self.id = kwargs['id']
                    if i == 'size':
                        self.width = kwargs['size']
                        self.height = kwargs['size']
                    if i == 'x':
                        self.x = kwargs['x']
                    if i == 'y':
                        self.y = kwargs['y']

    def to_dictionary(self):
        """  returns the dictionary
        representation of a Square
        """
        dictionary = {}
        dictionary['id'] = self.id
        dictionary['size'] = self.width
        dictionary['x'] = self.x
        dictionary['y'] = self.y
        return dictionary

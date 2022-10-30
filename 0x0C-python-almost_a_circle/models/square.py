#!/usr/bin/python3
'''Defines a Square class that inherits from a Rectangle class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A Square class that inherits from a Rectangle class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initialization method'''
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('width must be an integer')
        if size <= 0:
            raise ValueError('width must be > 0')
        self.__size = self.width = self.height = size

    def __str__(self):
        '''returns a string representation of a Square instance.'''
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

#!/usr/bin/python3
'''Defines a Square class that inherits from a Rectangle class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A Square class that inherits from a Rectangle class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initialization method'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''returns a string representation of a Square instance.'''
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

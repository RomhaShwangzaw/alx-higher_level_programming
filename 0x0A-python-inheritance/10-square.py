#!/usr/bin/python3
'''A Square module'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    '''A Square class'''

    def __init__(self, size):
        '''Initialization method'''
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''calculates the area of a square'''
        return self._size * self.__size

    def __str__(self):
        '''returns a string description of the rectangle'''
        return "[Rectangle] " + str(self.__size) + "/" + str(self.__size)

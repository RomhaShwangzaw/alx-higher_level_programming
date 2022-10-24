#!/usr/bin/python3
'''A Square module'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A Square class'''

    def __init__(self, size):
        '''Initialization method'''
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''calculates the area of a square'''
        return self.__size * self.__size

    def __str__(self):
        '''returns a string description of a square'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)

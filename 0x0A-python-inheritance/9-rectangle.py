#!/usr/bin/python3
'''A Rectangle module'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A Rectangle class'''

    def __init__(self, width, height):
        '''Initialization method'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''calculates the area of a rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''returns a string description of the rectangle'''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

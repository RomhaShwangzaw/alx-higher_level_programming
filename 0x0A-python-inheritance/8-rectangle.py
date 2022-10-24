#!/usr/bin/python3
'''A Rectangle module'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A Rectangle class'''

    def __init__(self, width, height):
        '''Initialization method'''
        integer_validator(self, "width", width)
        integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

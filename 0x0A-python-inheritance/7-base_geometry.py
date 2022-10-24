#!/usr/bin/python3
''' A Base Geometry module'''


class BaseGeometry:
    ''' A BaseGeometry class'''

    def area(self):
        '''raises an Exception with the message area() is not implemented'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''validates value

        you can assume name is always a string

        if value is not an integer: raise a TypeError exception,
        with the message <name> must be an integer

        if value is less or equal to 0: raise a ValueError exception
        with the message <name> must be greater than 0
        '''
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')

        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')

#!/usr/bin/python3
''' A Rectangle Module '''


class Rectangle:
    ''' A class that defines a rectangle '''

    def __init__(self, width=0, height=0):
        ''' Initialization module '''
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        ''' calculates the area of the rectangle '''
        return self.__height * self.__width

    def perimeter(self):
        ''' calculates the perimeter of the rectangle '''
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        ''' Returns a string representing the rectangle '''
        if self.__height == 0 or self.__width == 0:
            return ""

        output = ""
        for i in range(self.__height):
            for j in range(self.__width):
                output += '#'
            if i != self.__height - 1:
                output += '\n'

        return output

    def __repr__(self):
        ''' Returns a string reprsentation of the rectangle
            that can be changed back to the rectangle object
            by using eval() method '''

        output = "Rectangle(" + str(self.__width) + ", "
        output += str(self.__height) + ")"
        return output

    def __del__(self):
        print('Bye rectangle...')

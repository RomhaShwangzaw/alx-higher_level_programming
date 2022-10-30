#!/usr/bin/python3
''' A module that defines a Rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class that inherits from the Base class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialization class'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        '''returns the area value of the Rectangle instance.'''
        return self.height * self.width

    def display(self):
        '''prints in stdout the Rectangle instance with the character #,
        by taking care of x and y
        '''
        for i in range(self.y):
            print()

        for i in range(self.height):
            for k in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        '''returns a string representation of a Rectangle instance.'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

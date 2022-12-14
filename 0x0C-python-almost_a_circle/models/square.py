#!/usr/bin/python3
'''Defines a Square class that inherits from a Rectangle class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A Square class that inherits from a Rectangle class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initialization method'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        '''returns a string representation of a Square instance.'''
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        '''assigns attributes:

        * *args is the list of arguments - no-keyworded arguments
            - 1st argument should be the id attribute
            - 2nd argument should be the size attribute
            - 3rd argument should be the x attribute
            - 4th argument should be the y attribute

        * **kwargs can be thought of as a double pointer to a dictionary:
            key/value (keyworded arguments)
        * **kwargs must be skipped if *args exists and is not empty
        * Each key in this dictionary represents an attribute to the instance

        '''
        if args is not None and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'size':
                    self.size = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v

    def to_dictionary(self):
        '''returns the dictionary representation of a Square:

        * This dictionary must contain:
            - id
            - size
            - x
            - y

        '''
        square_dict = {}
        square_dict['id'] = self.id
        square_dict['size'] = self.size
        square_dict['x'] = self.x
        square_dict['y'] = self.y
        return square_dict

#!/usr/bin/python3
'''Defines a Student class'''


class Student:
    '''A Student class'''
    def __init__(self, first_name, last_name, age):
        '''Initialization function'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a dictionary representation of a Student instance'''
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            my_dict = dict()
            for i in attrs:
                if i in self.__dict__:
                    my_dict[i] = self.__dict__[i]

            return my_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        '''replaces all attributes of the Student instance.'''
        for k, v in json.items():
            setattr(self, k, v)

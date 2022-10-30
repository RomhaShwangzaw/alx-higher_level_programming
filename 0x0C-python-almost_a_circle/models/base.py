#!/usr/bin/python3
'''Defines a Base class for all other classes'''
import json


class Base:
    '''A Base class that defines the 'id' attribute
    for the rest of the classes
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initializes the 'id' attribute'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries:

        - list_dictionaries is a list of dictionaries
        - If list_dictionaries is None or empty, return the string: "[]"
        - Otherwise, return the JSON string representation of list_dictionaries

        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

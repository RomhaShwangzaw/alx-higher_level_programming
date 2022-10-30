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

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file:

        - list_objs is a list of instances who inherits of Base - example:
                            list of Rectangle or list of Square instances
        - If list_objs is None, save an empty list
        - The filename must be: <Class name>.json - example: Rectangle.json
        - You must use the static method to_json_string (created before)
        - You must overwrite the file if it already exists

        '''
        filename = cls.__name__ + ".json"
        list_dictionaries = []
        if list_objs is not None:
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())

        with open(filename, 'w', encoding='utf-8') as f:
            json_str = Base.to_json_string(list_dictionaries)
            f.write(json_str)

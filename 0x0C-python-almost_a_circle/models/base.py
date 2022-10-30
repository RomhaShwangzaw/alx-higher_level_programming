#!/usr/bin/python3
'''Defines a Base class for all other classes'''
import json
from os.path import exists


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

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation json_string:

        - json_string is a string representing a list of dictionaries
        - If json_string is None or empty, return an empty list
        - Otherwise, return the list represented by json_string

        '''
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set:

        - **dictionary can be thought of as a double pointer to a dictionary
        - To use the update method to assign all attributes,
          you must create a “dummy” instance before:

            * Create a Rectangle or Square instance with “dummy” mandatory
              attributes (width, height, size, etc.)
            * Call update instance method to this “dummy” instance to
              apply your real values

        - You must use the method def update(self, *args, **kwargs)
        - **dictionary must be used as **kwargs of the method update
        - You are not allowed to use eval

        '''
        obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances:

        - The filename must be: <Class name>.json - example: Rectangle.json
        - If the file doesn’t exist, return an empty list
        - Otherwise, return a list of instances - the type of these instances
          depends on cls (current class using this method)
        - You must use the from_json_string and create methods
          (implemented previously)

        '''
        filename = cls.__name__ + ".json"
        list_objs = []

        if not exists(filename):
            return list_objs

        with open(filename, encoding='utf-8') as f:
            json_str = f.read()

        list_dictionaries = cls.from_json_string(json_str)
        for dictionary in list_dictionaries:
            obj = cls.create(**dictionary)
            list_objs.append(obj)

        return list_objs

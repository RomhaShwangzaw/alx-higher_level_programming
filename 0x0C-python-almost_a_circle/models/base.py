#!/usr/bin/python3
'''Defines a Base class for all other classes'''
import json
from os.path import exists
import csv
import turtle


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
        if dictionary and dictionary != {}:
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Write the CSV serialization of a list of objects to a file.

        - The filename must be: <Class name>.csv - example: Rectangle.csv
        - Has the same behavior as the JSON serialization
        - Format of the CSV:
            * Rectangle: <id>,<width>,<height>,<x>,<y>
            * Square: <id>,<size>,<x>,<y>

        '''
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            if list_objs is None or list_objs == []:
                f.write('[]')
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        '''Return a list of classes instantiated from a CSV file.

        - Reads from `<cls.__name__>.csv`.

        - Returns:
            * If the file does not exist - an empty list.
            * Otherwise - a list of instantiated classes.

        '''
        filename = cls.__name__ + ".csv"
        list_objs = []

        if not exists(filename):
            return list_objs

        with open(filename, 'r', newline='') as f:
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            else:
                fieldnames = ['id', 'size', 'x', 'y']
            list_dictionaries = csv.DictReader(f, fieldnames=fieldnames)
            list_dictionaries = [dict([k, int(v)] for k, v in d.items())
                                 for d in list_dictionaries]

        for dictionary in list_dictionaries:
            obj = cls.create(**dictionary)
            list_objs.append(obj)

        return list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''opens a window and draws all the Rectangles and Squares:

        - You must use the Turtle graphics module
        - To install it: sudo apt-get install python3-tk

        '''
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

#!/usr/bin/python3
'''Defines a method that alters a file'''


def append_after(filename="", search_string="", new_string=""):
    '''inserts a line of text to a file, after each line
    containing a specific string
    '''
    text = ""
    with open(filename, encoding='utf-8') as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, 'w', encoding='utf-8') as w:
        w.write(text)

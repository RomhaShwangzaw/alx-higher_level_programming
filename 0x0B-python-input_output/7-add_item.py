#!/usr/bin/python3
'''Defines a script that adds all arguments to a Python list,
and then save them to a file.
'''
import json
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if os.path.isfile('add_item.json'):
    with open('add_item.json', encoding='utf-8') as f:
        my_list = json.load(f)
else:
    my_list = []

for i in sys.argv[1:]:
    my_list.append(i)

with open('add_item.json', 'w', encoding='utf-8') as f:
    json.dump(my_list, f)

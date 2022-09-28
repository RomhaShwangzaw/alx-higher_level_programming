#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    my_list = []
    for k, v in a_dictionary.items():
        if v == value:
            my_list.append(k)

    for i in my_list:
        a_dictionary.pop(i)

    return a_dictionary

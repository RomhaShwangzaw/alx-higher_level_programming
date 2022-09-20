#!/usr/bin/python3
def uppercase(str):
    new_str = ""

    for c in str:
        x = ord(c)
        if x >= 97 and x <= 122:
            new_str += chr(x - 32)
        else:
            new_str += c

    print(new_str)

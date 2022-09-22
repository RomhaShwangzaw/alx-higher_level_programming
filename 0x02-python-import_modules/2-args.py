#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print("1 argument:")
    else:
        print(f"{argc - 1} arguments:")

    i = 0
    for arg in sys.argv:
        if i != 0:
            print(f"{i}: {arg}")
        i += 1

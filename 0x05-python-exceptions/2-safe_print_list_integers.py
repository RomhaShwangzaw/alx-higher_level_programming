#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = -1
    j = 0

    while x > 0:
        try:
            x -= 1
            i += 1
            print("{:d}".format(my_list[i]), end="")
            j += 1

        except (ValueError, TypeError):
            continue

    print()
    return j

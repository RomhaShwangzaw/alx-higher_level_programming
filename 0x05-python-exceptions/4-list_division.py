#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    i = 0

    while list_length > 0:
        try:
            div = my_list_1[i] / my_list_2[i]
            res_list.append(div)
        except (ValueError, TypeError):
            print("wrong type")
            res_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            res_list.append(0)
        except IndexError:
            print("out of range")
            res_list.append(0)
        finally:
            i += 1
            list_length -= 1

    return res_list

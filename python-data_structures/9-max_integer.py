#!/usr/bin/python3


def max_integer(my_list=[]):
    max_num = 0
    if not my_list:
        return None

    for i in my_list:
        if i > max_num:
            max_num = i
    return(max_num)

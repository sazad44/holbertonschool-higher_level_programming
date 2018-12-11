#!/usr/bin/python3
def max_integer(my_list=[]):
    try:
        if not len(my_list):
            return None
        max = 0
        for i in my_list:
            if i > max:
                max = i
        return max
    except TypeError:
        return

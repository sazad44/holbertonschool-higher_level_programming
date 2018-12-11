#!/usr/bin/python3
def max_integer(my_list=[]):
    if isinstance(my_list, list) and not isinstance(my_list, str):
        if not len(my_list):
            return None
        max = my_list[0]
        for i in my_list:
            if i > max:
                max = i
        return max
    else:
        return None

#!/usr/bin/python3
def weight_average(my_list=[]):
    if isinstance(my_list, list) and len(my_list):
        numer = sum([e[0] * e[1] for e in my_list])
        denom = sum([e[1] for e in my_list])
        return (numer/denom)
    return 0

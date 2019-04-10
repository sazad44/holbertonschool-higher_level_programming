#!/usr/bin/python3
# Function to find peak of list passed in


def find_peak(list_of_integers):
    """Function finds peak of list passed in"""
    list_of_integers = tuple(list_of_integers)
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    halfIndex = int((len(list_of_integers) - 1) / 2)
    if list_of_integers[halfIndex] > list_of_integers[halfIndex + 1]\
       and list_of_integers[halfIndex] > list_of_integers[halfIndex - 1]:
        return list_of_integers[halfIndex]
    resr = find_peak(list_of_integers[halfIndex + 1:])
    resl = find_peak(list_of_integers[:halfIndex + 1])
    if resr and (resr > resl):
        return resr
    else:
        return resl

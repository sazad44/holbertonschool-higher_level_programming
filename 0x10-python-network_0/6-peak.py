#!/usr/bin/python3
# Function to find peak of list passed in


def find_peak(list_of_integers):
    """Function finds peak of list passed in"""
    loi = tuple(list_of_integers)
    if len(loi) == 0:
        return None
    elif len(loi) <= 2:
        return max(loi)
    elif loi[0] > loi[1]:
        return loi[0]
    elif loi[-1] > loi[-2]:
        return loi[-1]
    halfIndex = int((len(loi) - 1) / 2)
    if loi[halfIndex] > loi[halfIndex + 1]\
       and loi[halfIndex] > loi[halfIndex - 1]:
        return loi[halfIndex]
    resr = find_peak(loi[halfIndex + 1:])
    if resr:
        return resr
    resl = find_peak(loi[:halfIndex + 1])
    return resl

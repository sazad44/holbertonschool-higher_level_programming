#!/usr/bin/python3
# Function to find peak of list passed in


def find_peak(list_of_integers):
    """Function finds peak of list passed in"""
    loi = list_of_integers
    if len(loi) == 0:
        return None
    elif len(loi) == 1:
        return loi[0]
    halfIndex = int((len(loi) - 1) / 2)
    if loi[halfIndex] > loi[halfIndex + 1]\
       and loi[halfIndex] > loi[halfIndex - 1]:
        return loi[halfIndex]
    resl = find_peak(loi[halfIndex + 1:])
    resr = find_peak(loi[:halfIndex + 1])
    if resl and resl > resr:
        return resl
    elif resr:
        return resr

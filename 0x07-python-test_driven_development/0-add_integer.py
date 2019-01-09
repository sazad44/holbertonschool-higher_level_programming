#!/usr/bin/python3
""" Add Integer Module

This module adds two integers and rounds floats, checking types as well.

"""


def add_integer(a, b=98):
    """add_integer function to add a and b
    Return: Result of a and b addition
    """
    try:
        sum = a + b
        return int(round(a)) + int(round(b))
    except TypeError:
        if isinstance(a, int):
            raise TypeError('b must be an integer')
        elif isinstance(b, int):
            raise TypeError('a must be an integer')

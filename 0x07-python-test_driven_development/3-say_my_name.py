#!/usr/bin/python3
"""Say My Name Module

This module takes in two inputs that are first and last name.
It prints them together in a statement of my name is.
"""


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))

#!/usr/bin/python3
"""2-is_same_class module"""


def is_same_class(obj, a_class):
    """is_same_class function determines if input is a specific instance of
    specified class
    """
    return type(obj) == a_class

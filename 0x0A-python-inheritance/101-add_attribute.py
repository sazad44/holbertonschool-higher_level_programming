#!/usr/bin/python3
"""101-add_attribute module"""


def add_attribute(obj, key, value):
    """add_attribute function"""
    if not isinstance(key, (str, int, tuple, float, bool)) or type(obj) == str:
        raise TypeError("can't add new attribute")
    else:
        obj.__dict__[key] = value

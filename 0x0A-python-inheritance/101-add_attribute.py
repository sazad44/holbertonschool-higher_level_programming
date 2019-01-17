#!/usr/bin/python3
"""101-add_attribute module"""


def add_attribute(obj, key, value):
    """add_attribute function"""
    if not isinstance(key, (int, str, tuple, float, bool, complex, range)):
        raise TypeError("can't add new attribute")
    elif not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        obj.__dict__[key] = value

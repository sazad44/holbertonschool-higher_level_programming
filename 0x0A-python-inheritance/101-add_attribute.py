#!/usr/bin/python3
"""101-add_attribute module"""


def add_attribute(obj, key, value):
    """add_attribute function"""
    try:
        obj.__dict__[key] = value
    except:
        raise TypeError("can't add new attribute")

#!/usr/bin/python3
"""4-inherits_from module"""


def inherits_from(obj, a_class):
    """inherits_from function to determine if the type of obj is inherited"""
    if not isinstance(obj, a_class):
        return isinstance(obj, a_class)

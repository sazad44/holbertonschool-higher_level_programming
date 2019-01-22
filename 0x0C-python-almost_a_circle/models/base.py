#!/usr/bin/python3
"""Base Class Module"""


class Base:
    """Base Class to manage id attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init magic method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

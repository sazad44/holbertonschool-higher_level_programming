#!/usr/bin/python3
"""7-base_geometry module"""


class BaseGeometry(object):
    """BaseGeometry Class"""
    def __init__(self):
        """init magic method"""
        pass

    def area(self):
        """area method raises exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """int validator method validates value as integer"""
        if isinstance(name, str):
            if type(value) != int:
                raise TypeError("{} must be an integer".format(str(name)))
            elif value <= 0:
                raise ValueError("{} must be greater than 0".format(str(name)))

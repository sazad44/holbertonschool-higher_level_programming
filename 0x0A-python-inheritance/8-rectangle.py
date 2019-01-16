#!/usr/bin/python3
"""base_geometry module"""

class BaseGeometry(object):
    """BaseGeometry Class"""

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

class Rectangle(BaseGeometry):
    """Rectangle Class"""

    def __init__(self, width, height):
        """init magic method initialization procedure"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

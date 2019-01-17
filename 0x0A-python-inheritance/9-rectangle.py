#!/usr/bin/python3
"""9-rectangle module"""


class BaseGeometry(object):
    """BaseGeometry Class"""

    def area(self):
        """area method raises exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """int validator method validates value as integer"""
        if isinstance(name, str):
            if not isinstance(value, int):
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

    def area(self):
        """area method calculates and returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """str magic method"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

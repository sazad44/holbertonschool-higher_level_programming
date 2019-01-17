#!/usr/bin/python3
"""11-square module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        """__init__ magic method"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """area method"""
        return self.__size ** 2

    def __str__(self):
        """__str__ magic method"""
        return "[Square] {}/{}".format(self.__size, self.__size)

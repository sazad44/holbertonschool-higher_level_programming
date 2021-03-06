#!/usr/bin/python3

"""0-rectangle module"""


class Rectangle():

    """Rectangle Class

    Attributes:
    width (int): width of rectangle
    height (int): height of rectangle
    """

    def __init__(self, width=0, height=0):
        """Instantiation Method"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """height getter method

        returns: value of private height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method

        changes private attribute height's value and error checks value
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @property
    def width(self):
        """width getter method

        returns: value of private width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method

        changes private attribute width's value and error checks value
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

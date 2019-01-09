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

    def area(self):
        """area method

        returns: area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """perimeter method

        returns: perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __repr__(self):
        """dunder str method

        returns a string that represents the class instantiation
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __str__(self):
        """dunder str method

        returns a string representation of the data in the class
        """
        ret = ""
        ret_str = ""
        if self.__width == 0 or self.__height == 0:
            return ret_str
        else:
            for i in range(self.height):
                for j in range(self.width):
                    ret += "#"
                ret_str += ret
                if i != self.height - 1:
                    ret_str += "\n"
                ret = ""
        return ret_str

    def __del__(self):
        """del method

        prints message on destruction of python object
        """
        print("Bye rectangle...")

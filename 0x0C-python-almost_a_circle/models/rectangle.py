#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init magic method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter function"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter function"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter function"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter function"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x getter function"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter function"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y getter function"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter function"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """area method"""
        return self.__width * self.__height

    def display(self):
        """display method"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """string magic method"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".\
        format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update method"""
        if len(args) > 0:
            attrl = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                if i > 0:
                    self.__dict__["_Rectangle__" + attrl[i]] = args[i]
                else:
                    self.__dict__[attrl[i]] = args[i]
        else:
            for key in kwargs:
                if key != "id":
                    self.__dict__["_Rectangle__" + key] = kwargs[key]
                else:
                    self.__dict__[key] = kwargs[key]

#!/usr/bin/python3
class Square:
    __size = 0
    """Square class for a text square.

    Attributes:
       __size: size of the square privately
    """
    def __init__(self, size=0, position=(0, 0)):
        """ __init__ method to initialize class

        Args:
        self: the object itself
        size (int): size of the square
        position (tuple): coordinates of square

        Returns: No Value
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if (not isinstance(position, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not isinstance(position[0], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif(not isinstance(position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """area method to calculate the area of the square

        Args:
        self: the object itself

        Returns: the area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """size method to retrieve size

        Args:
        self: the object itself

        Returns: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size method to change size

        Args:
        self: the object itself
        value: the value to change size to

        Returns: the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """my_print method to print square

        Args:
        self: the object itself

        Returns: No Value just prints
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """position method to get value of private position attribute

        Args:
        self: the object itself

        Return: value of private position variable
        """
        return self.__position

    @position.setter
    def position(self, value):
        """position method to set value of private position variable

        Args:
        self: the object itself
        value (tuple): the new value for position to be applied

        Return: No Value
        """
        if (not isinstance(position, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not isinstance(position[0], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif(not isinstance(position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

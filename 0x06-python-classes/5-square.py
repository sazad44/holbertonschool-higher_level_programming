#!/usr/bin/python3
class Square:
    __size = 0
    """Square class for a text square.

    Attributes:
       __size: size of the square privately
    """
    def __init__(self, size=0):
        """ __init__ method to initialize class

        Args:
        self: the object itself
        size (int): size of the square

        Returns: No Value
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

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
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

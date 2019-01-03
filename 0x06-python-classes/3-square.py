#!/usr/bin/python3
class Square:
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

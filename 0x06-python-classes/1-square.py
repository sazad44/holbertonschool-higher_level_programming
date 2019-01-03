#!/usr/bin/python3
class Square:
    """Square class for a text square.

    Attributes:
       __size: size of the square privately
    """
    __size = 0

    def __init__(self, size):
        """__init__ method to initialize class

        Args:
        self: the object itself
        size (int): the size of the square

        Returns: No Value
        """
        self.__size = size

#!/usr/bin/python3
"""Print Square Module

This module prints a square according to the input specificiations.
It prints out a square or error depending on the input.
"""

def print_square(size):
    """print_square function prints square according to size parameter
    Returns nothing
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise TypeError('size must be >= 0')
    elif size == 0:
        print()
    else:
        for i in range(size):
            for j in range(size):
                print('#', end='')
            print()

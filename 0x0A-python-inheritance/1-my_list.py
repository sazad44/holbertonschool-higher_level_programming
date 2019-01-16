#!/usr/bin/python3
"""1-my_list module containing class definition"""
class MyList(list):
    """MyList class subclass of list

    Attributes:
    print_sorted: prints the list in a sorted fashion
    """
    def print_sorted(self):
        """print_sorted method prints list sorted"""
        print(sorted(self))

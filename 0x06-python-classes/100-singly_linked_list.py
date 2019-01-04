#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        pass

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:

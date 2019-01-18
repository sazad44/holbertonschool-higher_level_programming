#!/usr/bin/python3
"""12-student module"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """init magic method"""
        if not isinstance(first_name, str):
            raise TypeError('first_name is of the wrong type')
        elif not isinstance(last_name, str):
            raise TypeError('last_name is of the wrong type')
        if type(age) != int:
            raise TypeError('age is of the wrong type')
        else:
            self.first_name = first_name
            self.last_name = last_name
            self.age = age

    def to_json(self, attrs=None):
        """to_json method"""
        retd = self.__dict__
        if type(attrs) == list:
            if not all(type(x) == str for x in attrs):
                return retd
            return {i: retd[i] for i in attrs if i in retd.keys()}
        else:
            return retd

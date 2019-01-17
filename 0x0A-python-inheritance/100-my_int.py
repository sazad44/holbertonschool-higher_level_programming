#!/usr/bin/python3
"""100-my_int module"""
class MyInt(int):
    """MyInt Class"""
    def __eq__(self, other):
        """eq magic method"""
        return False

    def __ne__(self, other):
        """ne magic method"""
        return True

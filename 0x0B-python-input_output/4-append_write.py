#!/usr/bin/python3
"""4-append_write module"""


def append_write(filename="", text=""):
    """append_write function"""
    with open(filename, "a") as f:
        return f.write(text)

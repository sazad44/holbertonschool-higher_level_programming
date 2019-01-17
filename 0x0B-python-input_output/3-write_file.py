#!/usr/bin/python3
"""3-write_file module"""


def write_file(filename="", text=""):
    """write_file function"""
    with open(filename, "w") as f:
        return f.write(text)

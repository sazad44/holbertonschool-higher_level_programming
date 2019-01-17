#!/usr/bin/python3
"""0-read_file module"""


def read_file(filename=""):
    """read_file function"""
    with open(filename) as f:
        print(f.read(), end="")

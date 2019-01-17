#!/usr/bin/python3
"""1-number_of_lines module"""


def number_of_lines(filename=""):
    """number_of_lines function"""
    with open(filename) as f:
        return len(f.readlines())

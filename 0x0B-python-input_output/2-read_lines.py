#!/usr/bin/python3
"""2-read_lines module"""


def read_lines(filename="", nb_lines=0):
    """read_lines function"""
    with open(filename) as f:
        if nb_lines <= 0 or nb_lines >= len(f.readlines()):
            print(f.read(), end="")
            return
    with open(filename) as f:
        for line in range(nb_lines):
            print(f.readline(), end="")

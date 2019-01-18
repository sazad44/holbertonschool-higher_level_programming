#!/usr/bin/python3
"""2-read_lines module"""


def read_lines(filename="", nb_lines=0):
    """read_lines function"""
    if type(filename) == str:
        with open(filename) as f:
            if type(nb_lines) != int:
                print(f.read(), end="")
                return
            elif nb_lines <= 0 or nb_lines >= len(f.readlines()):
                print(f.read(), end="")
                return
        with open(filename) as f:
            for line in range(nb_lines):
                print(f.readline(), end="")

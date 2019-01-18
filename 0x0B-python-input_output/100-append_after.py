#!/usr/bin/python3
"""100-append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """append_after function"""
    with open(filename, "r") as f:
        rf = []
        nb_lines = len(f.readlines())
        f.seek(0)
        for i in range(nb_lines):
            line = f.readline()
            rf.append(line)
            if search_string in line:
                rf.append(new_string)
    with open(filename, "w") as f:
        f.writelines(rf)

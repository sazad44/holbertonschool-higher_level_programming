#!/usr/bin/python3
"""14-pascal_triangle module"""


def pascal_triangle(n):
    """pascal_triangle function"""
    retl = []
    if n <= 0:
        return retl
    for i in range(n):
        if i < 2:
            retl.append([1] * (i + 1))
        else:
            appl = [1]
            appl.extend([retl[i - 1][j] + retl[i - 1][j + 1]
                         for j in range(len(retl[i - 1]) - 1)])
            appl.append(1)
            retl.append(appl)
    return retl

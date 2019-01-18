#!/usr/bin/python3

import sys

try:
    i = 0
    fs_sum = s_200 = s_401 = s_403 = s_404 = s_405 = s_500 = 0
    while (True):
        if (i % 10 == 0 and i != 0):
            print("File size: {:d}".format(fs_sum))
            print("200: {:d}".format(s_200))
            print("401: {:d}".format(s_401))
            print("403: {:d}".format(s_403))
            print("404: {:d}".format(s_404))
            print("405: {:d}".format(s_405))
            print("500: {:d}".format(s_500))
        buf_line = sys.stdin.readline()
        split_buf = buf_line.split()
        fs_sum += int(split_buf[-1])
        s_code = split_buf[-2]
        if s_code == "200":
            s_200 += 1
        elif s_code == "401":
            s_200 += 1
        elif s_code == "403":
            s_200 += 1
        elif s_code == "404":
            s_404 += 1
        elif s_code == "405":
            s_405 += 1
        elif s_code == "500":
            s_500 += 1
        i += 1
except KeyboardInterrupt as k:
    print("File size: {:d}".format(fs_sum))
    print("200: {:d}".format(s_200))
    print("401: {:d}".format(s_401))
    print("403: {:d}".format(s_403))
    print("404: {:d}".format(s_404))
    print("405: {:d}".format(s_405))
    print("500: {:d}".format(s_500))

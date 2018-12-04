#!/usr/bin/python3
for x in range(10):
    for y in range(10):
        if y > x:
            print("{}".format(x), end="")
            print("{}".format(y), end="")
            if x == 8 and y == 9:
                print("".format())
            else:
                print("".format(), end=", ")

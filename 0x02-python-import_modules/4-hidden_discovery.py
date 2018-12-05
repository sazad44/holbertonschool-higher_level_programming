#!/usr/bin/python3
import hidden_4
for x in dir(hidden_4):
    if not x.startswith("__"):
        print("{}".format(x))

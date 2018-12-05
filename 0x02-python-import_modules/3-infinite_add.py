#!/usr/bin/python3
import sys
sum = 0
for x in range(1, len(sys.argv)):
    sum += int(sys.argv[x])
print("{}".format(sum))

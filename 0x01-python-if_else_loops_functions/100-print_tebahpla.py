#!/usr/bin/python3
for x in range(ord('z'), ord('a') - 1, -1):
    if (x % 2 != 0):
        i = x - ord('a') + ord('A')
    else:
        i = x
    print("{:c}".format(i), end="")

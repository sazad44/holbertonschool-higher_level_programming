#!/usr/bin/python3
def no_c(my_string):
    i = 0
    for c in my_string:
        if (c is 'c') or (c is 'C'):
            my_string = my_string[:i] + my_string[i + 1:]
            i -= 1
        i += 1
    return (my_string)

#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except (ValueError, TypeError, ZeroDivisionError, IndexError) as Err:
        sys.stderr.write("Exception: " + Err.args[0] + "\n")
        return None

#!/usr/bin/python3
def common_elements(set_1, set_2):
    if isinstance(set_1, set) and isinstance(set_2, set):
        new_set = {e for e in set_1 if e in set_2}
        return new_set
    return set()

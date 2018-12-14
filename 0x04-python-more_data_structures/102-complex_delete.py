#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if isinstance(a_dictionary, dict) and len(a_dictionary):
        if value in a_dictionary.values():
            k_tup = ()
            for k in a_dictionary:
                if a_dictionary[k] == value:
                    k_tup += k,
            for e in k_tup:
                del a_dictionary[e]
        return a_dictionary

#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict) and len(a_dictionary):
        comp = max([v for v in a_dictionary.values()])
        for k in a_dictionary.keys():
            if a_dictionary[k] == comp:
                return k

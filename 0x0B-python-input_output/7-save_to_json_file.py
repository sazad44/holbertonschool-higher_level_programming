#!/usr/bin/python3
"""7-save_to_json_file module"""


def save_to_json_file(my_obj, filename):
    """save_to_json_file function"""
    import json

    with open(filename, "w") as f:
        return f.write(json.dumps(my_obj))

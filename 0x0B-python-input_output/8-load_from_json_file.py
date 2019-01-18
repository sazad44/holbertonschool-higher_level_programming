#!/usr/bin/python3
"""8-load_from_json_file module"""


def load_from_json_file(filename):
    """load_from_json_file function"""
    import json

    with open(filename, "r") as f:
        return json.loads(f.read())

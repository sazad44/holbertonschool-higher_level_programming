#!/usr/bin/python3
"""Base Class Module"""
import json


class Base:
    """Base Class to manage id attribute"""
    __nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string static method"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """from_json_string static method"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file method"""
        if list_objs is None:
            with open(cls.__name__ + ".json", "w+") as f:
                f.write("[]")
        with open(cls.__name__ + ".json", "w+") as f:
            f.write(Base.to_json_string([x.to_dictionary() for x in list_objs]))

    def __init__(self, id=None):
        """init magic method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

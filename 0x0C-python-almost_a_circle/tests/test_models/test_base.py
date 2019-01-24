#!/usr/bin/python3
"""Base Class Test Module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):

    def test_noinput(self):
        """test_noinput"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_wronginput(self):
        """test_wronginput"""
        b1 = Base()
        self.assertEqual(b1.id, 4)
        b2 = Base("wrong")
        self.assertEqual(b2.id, "wrong")

    def test_to_json_string(self):
        """test_to_json_string"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r1_dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([r1_dictionary])
        self.assertTrue(type(r1_dictionary) == dict)
        self.assertTrue(type(json_dictionary) == str)
        json_dictionary = Base.to_json_string([])
        self.assertTrue(json_dictionary == "[]")

    def test_string_to_file(self):
        """test_string_to_file method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, id=1)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "w+") as f:
            self.assertTrue(type(f.read()) == str)

    def test_from_json_string(self):
        """test_from_json_string method test"""
        json_list_input = Rectangle.to_json_string([{"hi":5, "hey":6}])
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(type(list_output) == list)

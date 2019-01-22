#!/usr/bin/python3
"""Base Class Test Module"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_noinput(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_wronginput(self):
        b1 = Base()
        self.assertEqual(b1.id, 4)
        b2 = Base("wrong")
        self.assertEqual(b2.id, "wrong")

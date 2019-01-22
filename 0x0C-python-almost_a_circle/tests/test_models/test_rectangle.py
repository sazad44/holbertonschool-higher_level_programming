#!/usr/bin/python3
"""Rectangle Test Module"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Rectangle Test Class"""
    def test_main_2(self):
        """test_main_2 method"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 6)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)

    def test_main_3(self):
        """test_main_3 method"""
        r1 = Rectangle(10, 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r4 = Rectangle(10, "2")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r4 = Rectangle("10", 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r4 = Rectangle(10, 2, "3")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r4 = Rectangle(10, 2, 3, "4")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.width = -10
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.height = -10
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.x = -10
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.y = -10
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.x = {}
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r4 = Rectangle(10, 2, 3, -1)

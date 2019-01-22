#!/usr/bin/python3
"""Rectangle Test Module"""
import unittest
import sys
import io
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Rectangle Test Class"""
    def test_main_2(self):
        """test_main_2 method"""
        r1_m = Rectangle(10, 2)
        self.assertEqual(r1_m.width, 10)
        self.assertEqual(r1_m.height, 2)
        r2_m = Rectangle(2, 10)
        self.assertEqual(r2_m.width, 2)
        self.assertEqual(r2_m.height, 10)
        r3_m = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3_m.width, 10)
        self.assertEqual(r3_m.height, 2)

    def test_exceptions(self):
        """test_exceptions method"""
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

    def test_area(self):
        """test_area method"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """test_display method"""
        r1 = Rectangle(4, 6)
        CO = io.StringIO()
        sys.stdout = CO
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(CO.getvalue(), "####\n####\n####\n####\n####\n####\n")
        r1 = Rectangle(2, 2)
        CO = io.StringIO()
        sys.stdout = CO
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(CO.getvalue(), "##\n##\n")

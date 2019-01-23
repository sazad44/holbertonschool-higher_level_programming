#!/usr/bin/python3
"""Square Test Module"""
import sys
import io
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """TestSquare Class"""
    def test_square(self):
        """test_square method"""
        s1 = Square(5, id=1)
        CO = io.StringIO()
        sys.stdout = CO
        print(s1)
        self.assertEqual(CO.getvalue(), "[Square] (1) 0/0 - 5\n")
        self.assertEqual(s1.area(), 25)
        CO = io.StringIO()
        sys.stdout = CO
        s1.display()
        self.assertEqual(CO.getvalue(), "#####\n#####\n#####\n#####\n#####\n")
        s2 = Square(2, 2, id=2)
        CO = io.StringIO()
        sys.stdout = CO
        print(s2)
        self.assertEqual(CO.getvalue(), "[Square] (2) 2/0 - 2\n")
        self.assertEqual(s2.area(), 4)
        CO = io.StringIO()
        sys.stdout = CO
        s2.display()
        self.assertEqual(CO.getvalue(), "  ##\n  ##\n")
        s3 = Square(3, 1, 3, id=3)
        CO = io.StringIO()
        sys.stdout = CO
        print(s3)
        self.assertEqual(CO.getvalue(), "[Square] (3) 1/3 - 3\n")
        self.assertEqual(s3.area(), 9)
        CO = io.StringIO()
        sys.stdout = CO
        s3.display()
        self.assertEqual(CO.getvalue(), "\n\n\n ###\n ###\n ###\n")

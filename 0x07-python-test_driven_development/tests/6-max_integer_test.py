#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """TestMaxInteger class is a unit testing class for the function max_integer
    """

    def test_max(self):
        """test_max method
        tests a normal list and if the function gets the max
        """
        self.assertEqual(max_integer([4, 6, 3, 5, 78, 4, 3, 4, 1, 9]), 78)

    def test_empty(self):
        """test_empty method
        tests function with empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_equal(self):
        """test_equal method
        tests function with list with duplicates
        """
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_error(self):
        """test_error method
        tests function in error situation
        """
        with self.assertRaises(TypeError):
            max_integer(['a', 3, 4])

    def test_none(self):
        """test_none method
        tests function when none is passed
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_negative(self):
        """test_negative method
        tests function if parts of the list are negative
        """
        self.assertEqual(max_integer([3, -4, 5, -6]), 5)

    def test_one_input(self):
        """test_one_input method
        tests function with one element in the list
        """
        self.assertEqual(max_integer([4]), 4)

    def test_ex1(self):
        """test_ex1 method
        tests function with first example
        """
        self.assertEqual(max_integer([5, 2, 3, 4]), 5)

    def test_one_neg(self):
        """test_ex2 method
        tests function with first example
        """
        self.assertEqual(max_integer([1, -3, 4, 2]), 4)

    def test_max_end(self):
        """test_ex2 method
        tests function with first example
        """
        self.assertEqual(max_integer([1, -3, 4, 6]), 6)

    def test_1neg(self):
        """test_ex2 method
        tests function with first example
        """
        self.assertEqual(max_integer([-3]), -3)

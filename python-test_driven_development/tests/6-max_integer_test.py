#!/usr/bin/python3
"""Unittest for max_integer."""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer."""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_sorted_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 3, 2, 1]), 9)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-8, -2, -5, -9]), -2)

    def test_same_numbers(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 0, 7, 3]), 7)


if __name__ == "__main__":
    unittest.main()

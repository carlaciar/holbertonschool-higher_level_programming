#!/usr/bin/python3
"""Unittests for max_integer(list=[])"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_one_element_list(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        # Calling with no argument should behave like empty list
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -5, -7, -9]), -5)

    def test_mixed_ints_and_floats(self):
        self.assertEqual(max_integer([1, 2.5, 2, 2.49]), 2.5)

    def test_all_equal(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_strings(self):
        # If the implementation supports iterables of strings,
        # it should return the lexicographically max string.
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_mixed_types_raises(self):
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])

    def test_large_integers(self):
        self.assertEqual(max_integer([1, 10**6, 999999]), 10**6)


if __name__ == '__main__':
    unittest.main()

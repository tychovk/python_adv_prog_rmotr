"""
Write a function that receives 2 numbers and returns the largest of them.
You can't use the builtin max function.
Example:
    max_of_two_numbers(2, 3)       # Should return 3
    max_of_two_numbers(7, 3)       # Should return 7
    max_of_two_numbers(6, 6)       # Should return 6
"""

def max_of_two_numbers(number_1, number_2):
    if number_1 > number_2:
        return number_1
    else:
        return number_2


# Don't change below this line! These tests should pass

import unittest

class MaxOfTwoNumbersTestCase(unittest.TestCase):
    def test_left_is_max(self):
        self.assertEqual(max_of_two_numbers(11, 3), 11)
        
    def test_right_is_max(self):
        self.assertEqual(max_of_two_numbers(10, 18), 18)

    def test_equal_numbers(self):
        self.assertEqual(max_of_two_numbers(3, 3), 3)
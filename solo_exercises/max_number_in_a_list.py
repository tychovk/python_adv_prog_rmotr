"""
Write a function that receives a list and returns the larger number in the list.
You can't use the `max` builtin function.
Example:
    max_in_list([7, 1, 5, 8, 0, 7, 9, 1, 7])
    > 9

Extras:
* Try with a for loop
* Try with a while loop
* Investigate special list methods or python libraries. You can use whatever you want now.
"""

#works!
def max_in_list(a_list):
    if a_list:
        highest = 0
        for x in a_list:
            if x > highest:
                highest = x
        return highest

    

# Don't change below this line! These tests should pass

import unittest

class MaxInListTestCase(unittest.TestCase):
    def test_max_in_first_position(self):
        self.assertEqual(max_in_list([11, 0, 9, 3, 7]), 11)

    def test_max_in_last_position(self):
        self.assertEqual(max_in_list([11, 0, 9, 3, 7, 38]), 38)

    def test_max_in_middle_position(self):
        self.assertEqual(max_in_list([11, 0, 91, 3, 7]), 91)

    def test_max_with_two_elements(self):
        self.assertEqual(max_in_list([19, 0]), 19)
        self.assertEqual(max_in_list([31, 32]), 32)
        
    def test_max_with_one_element(self):
        self.assertEqual(max_in_list([5]), 5)
    
    def test_max_with_empty_list(self):
        self.assertEqual(max_in_list([]), None)
        
unittest.main()
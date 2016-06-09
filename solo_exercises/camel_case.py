"""
Write a function that receives a string and returns a camel case version of it.
Example:
    camel_case('hello world')  # Hello World
"""


def camel_case(a_string):
        camel_a_list = ' '.join([word.capitalize() for word in a_string.split(" ")])
        return camel_a_list

# Don't change below this line! These tests should pass

import unittest

class CamelCaseTestCase(unittest.TestCase):
    def test_word_with_spaces(self):
        self.assertEqual(camel_case("testing 123 hello"), 'Testing 123 Hello')
        
    def test_single_word(self):
        self.assertEqual(camel_case("testing"), 'Testing')

    def test_empty_string(self):
        self.assertEqual(camel_case(""), '')
		

unittest.main()
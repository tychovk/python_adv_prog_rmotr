import unittest

"""
Build a calculator using only static and class methods. This is the way it should work:


    Calculator.add(2, 4)  # 6
    Calculator.subtract(8, 1)  # 7
    Calculator.multiply(3, 5)  # 15
    Calculator.divide(5, 2)  # 2.5

Note that I've never created an instance of the calculator. I'm using the regular class.

One final addition. The `subtract` method **must** be implemented using the `add` method. Something like this:

subtract = add(x, y * -1) 
"""

class Calculator:
    
    @staticmethod
    def add(n1, n2):
        return n1 + n2
        
    @staticmethod
    def subtract(n1, n2):
        return Calculator.add(n1, n2 * -1)
    
    @staticmethod    
    def multiply(n1, n2):
        return n1 * n2
    
    @staticmethod    
    def divide(n1, n2): 
        return n1 / float(n2)
        
        
class CalculatorTestCase(unittest.TestCase):

    def test_add(self):
       self.assertEqual(Calculator.add(5, 2), 7)
       
    def test_subtract(self):
       self.assertEqual(Calculator.subtract(5, 2), 3)
       
    def test_multiply(self):
       self.assertEqual(Calculator.multiply(7, 9), 63)
       
    def test_divide(self):
       self.assertEqual(Calculator.divide(9, 3), 3.0)
       
    def test_divide_decimal(self):
       self.assertEqual(Calculator.divide(9, 2), 4.5)
       
unittest.main()


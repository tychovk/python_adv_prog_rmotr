import unittest


class Calculator:
    def __init__(self):
        hurr = []
        
    def add(self, n1, n2):
        return n1 + n2
        
    def subtract(self, n1, n2):
        return n1 - n2
        
    def multiply(self, n1, n2):
        return n1 * n2
        
    def divide(self, n1, n2): 
        return n1 / n2
        
        
        
        
class CalculatorTestCase(unittest.TestCase):
    
    def setUp(self):
        self.c = Calculator()
        
    def test_add(self):
       self.assertEqual(self.c.add(5, 2), 7)
       
    def test_subtract(self):
       self.assertEqual(self.c.subtract(5, 2), 3)
       
    def test_multiply(self):
       self.assertEqual(self.c.multiply(7, 9), 63)
       
    def test_divide(self):
       self.assertEqual(self.c.divide(9, 3), 3.0)
       
    def test_divide_decimal(self):
       self.assertEqual(self.c.divide(9, 2), 4.5)
       
       
calculator = Calculator()

calculator.add(2, 4)  # 6
calculator.subtract(8, 1)  # 7
calculator.multiply(3, 5)  # 15
calculator.divide(5, 2)  # 2.5


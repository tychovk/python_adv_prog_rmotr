def calculator(operation, num1, num2):
    
    if operation == 'sum':
        return num1 + num2
    elif operation == 'subtraction':
        return num1 - num2
    else: 
        #raise AttributeError
        #raise AttributeError()
        raise AttributeError("Invalid operation")


import unittest

class BasicCalculatorTestCase(unittest.TestCase):
    def test_calculator_add(self):
        result = calculator('sum', 2, 3)
        self.assertEqual(result, 5)

    def test_calculator_subtract(self):
        result = calculator('subtraction', 7, 5)
        self.assertEqual(result, 2)
        
    def test_invalid_operation_raises_attribute_error(self):
        calculator('invalid-op!', 7, 5)
        # with self.assertRaises(AttributeError):
        #     calculator('invalid-op!', 7, 5)


if __name__ == '__main__':
    unittest.main()
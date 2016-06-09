"""
Implement an @only_int_arguments decorator for the "sum_integers(*args)" function. It must
validate that all arguments passed to the function are integers, or raise
ValueError otherwise.

NOTE: Use a class decorator, not a function.

Examples:
    sum_integers(2, 4, 6, 8)  # 20
    sum_integers("a", "b", "c")  # ValueError
"""


class only_int_arguments(object):
    def __init__(self, original_function):
        self.original_function = original_function

        
    def __call__(self, *args):
        for arg in args:
            x = isinstance(arg, int)
            if x is False:
                raise ValueError
        return self.original_function(*args)
        

"""

def only_int_arguments(old_f):
    def new_f(*args):
        for arg in args:
            x = isinstance(arg, int)
            if x is False:
                raise ValueError
        return old_f(*args)
    return new_f
"""

@only_int_arguments
def sum_integers(*args):
    return sum(list(args))

    
if __name__ == "__main__":
    import unittest
    class AssignmentTestCase(unittest.TestCase):
  
        def test_1(self):
            self.assertEqual(sum_integers(2, 5, 3), 10)
            
        def test_2(self):
            with self.assertRaises(ValueError):
                sum_integers("Hello", "world")
            
    unittest.main()
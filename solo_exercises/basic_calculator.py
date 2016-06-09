"""
Write a function that receives 2 numbers and performs simple calculations
(additions, subtractions, multiplications and divisions)
based on a string parameter.
    calculator(2, 3, 'add')       # Should return 5
    calculator(7, 3, 'subtract')  # Should return 4
    calculator(2, 7, 'multiply')  # Should return 14
    calculator(8, 4, 'divide')    # Should return 2
    calculator(5, 2, 'divide')    # Should return 2.5 ATTENTION!
"""


def calculator(param1, param2, operation):
    if operation == 'add':
        return param1 + param2
    if operation == 'subtract':
        return param1 - param2          
    if operation == 'divide':
        division = str(param1 / param2)
        if division[-1] == '0':
            return division[:-2]
        else:
            return float(division)
    if operation == 'multiply':
        return param1 * param2                
    
    
print (calculator(2, 3, 'add'))       # Should return 5
print (calculator(7, 3, 'subtract') ) # Should return 4
print (calculator(2, 7, 'multiply'))  # Should return 14
print (calculator(8, 4, 'divide')  )  # Should return 2
print (calculator(5, 2, 'divide')  )  # Should return 2.5 ATTENTION!
"""
Write a function that combines list comprehensions and lambdas
to transform temperatures given in celsius to fahrenheit.

Example:
    to_fahrenheit([0, 10, 25, 30, 100]) # [32.0, 50.0, 77.0, 86.0, 212.0]

"""

def to_fahrenheit(a_list):
    conversion = [(x * (9/5) + 32) for x in a_list]
    return conversion
    
    
    
    
    
print (to_fahrenheit([0, 10, 25, 30, 100])) # [32.0, 50.0, 77.0, 86.0, 212.0]

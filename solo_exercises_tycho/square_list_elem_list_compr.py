"""
Write a function that receives a list of integers and
returns a list with all the elements squared using
list comprehensions.

Example:
    square_elements([1, 2, 3, 4, 5]) # [1, 4, 9, 16, 25]

"""

def square_elements(a_list):
    return [x**2 for x in a_list]
    
    
    
    

print (square_elements([1, 2, 3, 4, 5])) # [1, 4, 9, 16, 25]
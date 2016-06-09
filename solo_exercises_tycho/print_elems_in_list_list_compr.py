"""
Write a function that receives a list and prints all its
items using a list comprehension.

Example:
    print_members(["Hello", 3, True, (1, 2)])

"""
import timeit



def print_members(a_list):
    print (' '.join(str(x) for x in a_list))
    
    
    
    
    
print_members(["Hello", 3, True, (1, 2)])
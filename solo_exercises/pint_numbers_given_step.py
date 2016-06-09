"""
Write a function that receives a starting number, an ending number (not inclusive)
and a step number, and print every number in the range separated by that step.
Example:
    print_numbers_with_a_step(1, 10, 2)
    > 1
    > 3
    > 5
    > 7
    > 9
Extra:
* Use a while loop
* Use a flag to denote if the ending number is inclusive or not:
    print_numbers_with_a_step(1, 10, 2, inclusive=True)
* Use ranges
"""

def print_numbers_with_a_step(start, end, step):
    while start < end:
        print (start)
        start += step
        
        
def print_numbers_with_a_step2(start, end, step):
    for x in range(start, end, step):
        print (x)
        
def print_numbers_with_a_step3(start, end, step, inclusive = True):
    if inclusive == True:
        end += 1
    for x in range(start, end, step):
        print (x)      
        
print (print_numbers_with_a_step2(1, 10, 2))
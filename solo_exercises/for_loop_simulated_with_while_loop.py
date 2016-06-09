"""
Write a function that receives a list and prints every element in the list
using a while loop.
Example:
    for_loop_simulated_with_while([3, 1, 2, 5])
    > 3
    > 1
    > 2
    > 5
"""

def for_loop_simulated_with_while(a_list):
    x = 0
    while x < len(a_list):
        print (a_list[x])
        x += 1
    return

print (for_loop_simulated_with_while([3, 1, 2, 5]))
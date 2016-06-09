"""
Write a function that receives a list and an element and returns how many occurrences
of that particular element are in the list.
**You can't use any function from the standard library.**

Example:
    occurrences([7, 1, 5, 8, 0, 7, 9, 1, 7], 7)  # The number 7 is repeated 3 times.
    > 3
Extras:
* Try with a for loop
* Try with a while loop
* Investigate special list methods or python libraries. You can use whatever you want now.
"""

def occurrences(a_list, an_element):
    counter = 0
    for x in a_list:
        if x == an_element:
            counter += 1
    return counter
    
def occurrences2(a_list, an_element):
    counter = 0
    x = 0
    while x < len(a_list):
        if a_list[x] == an_element:
            counter += 1
        x += 1
    return counter
    
    
def occurrences3(a_list, an_element):
    counter = a_list.count(an_element)
    return counter
    
print (occurrences3([7, 1, 5, 8, 0, 7, 9, 1, 7], 7))
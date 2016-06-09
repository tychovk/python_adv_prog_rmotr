"""
Write a function that takes a list value as an argument
and returns a string with all the items separated
by a comma and a space, with and inserted before the last item.

Example: see test cases.
"""

def comma_code(a_list):
    if len(a_list) == 1:
        return a_list[0]
    else:
        if isinstance(a_list, list):
            answer = ', '.join(str(x) for x in a_list[:-1])
            answer = "{} and {}".format(answer, a_list[-1])
            return answer
        else:
            return "The variable wasn't a list."
            
            
        
a_list = ["skdlsdfi", "sldfkjsodfi", 383984]

print (comma_code(a_list))
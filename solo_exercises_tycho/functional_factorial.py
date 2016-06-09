"""
The objective of this assignment is to write a factorial function (https://en.wikipedia.org/wiki/Factorial).

In order to do that we'll define 2 helper functions:
 * factorial_terms: will receive a number and return the
                            list of terms to compute the factorial.
 * compute_factorial: Will receive a list of terms and compute de factorial.
                                *You must use the `reduce` function*

Finally, the `factorial` function will get a number and using both helper functions will compute
the answer. The `factorial` function can have just 1 line.

Use the tests to see the complete specification of what you're required to write.

"""

def factorial_terms(a_number):
    if a_number < 0:
        raise AttributeError("The inserted number should be positive.")
    n = a_number + 1
    return range(0,n)[1:]


def compute_factorial(terms):
    if terms == []:
        raise AttributeError("terms was empty")
    x = 1
    for num in terms:
        x *= num
    return x
    
    
def factorial(number):
    return compute_factorial(factorial_terms(number))
    
print ("the factorial answer", factorial(5))

print (factorial(0))



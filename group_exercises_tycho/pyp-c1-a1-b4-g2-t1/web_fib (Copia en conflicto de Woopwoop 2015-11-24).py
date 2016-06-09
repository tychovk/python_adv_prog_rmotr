"""
def F():
    a,b = 0,1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b
        

def SubFib(startNumber, endNumber):
    for cur in F():
        if cur > endNumber: return
        if cur >= startNumber:
            yield cur

for i in SubFib(10, 200):
    print (i)
"""

        
        

def SubFib(startNumber, endNumber):
    for cur in F():
        if cur > endNumber: return
        if cur >= startNumber:
            yield cur

'''
for i in F(100):
    print (i)            
'''            
#iteration:
# 1, 2, 3, 4, 5
#list index:
#0, 1, 2, 3, 4 
#fib number
#0, 1, 1, 2, 3

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped



   
def main():
    import timeit
    print(timeit.timeit("F(100))"))

def F(end_term):
    a,b,c = 0,1,3
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b
        c += 1
        if c == end_term:
            break



def get_f(end_term):
    x = [y for y in F(end_term)]
    return x[-1]
        





import timeit
result = timeit.Timer('get_f(95000)', 'from __main__ import F, get_f').timeit(1)
print (result)
   
"""
short_list = range(10)
wrapped = wrapper(F, short_list)
print (timeit.timeit(wrapped, number = 1000))

long_list = range(100)
wrapped = wrapper(F, long_list)
print (timeit.timeit(wrapped, number = 10000))
"""



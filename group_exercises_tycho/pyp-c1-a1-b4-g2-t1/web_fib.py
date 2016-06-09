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
        


def memoize(f):
  cache = {}
  def decorated_function(*args):
      if args in cache:
          return cache[args]
      else:
          cache[args] = f(*args)
          return cache[args]
  return decorated_function




def a_function(an_argument):
    return an_argument**an_argument**an_argument #for example



import timeit
average_out_of = 10
the_argument = 50000
result = timeit.Timer('get_f({})'.format(the_argument), 'from __main__ import F, get_f').timeit(average_out_of)

print ("Out of ", result)
   
result = timeit.Timer('memoize({})'.format(the_argument), 'from __main__ import memoize').timeit(10)
print ("memoize", result)

'''implementing a memoized recursive fibonacci
'''
​
​
class memoize(dict):
    def __init__(self, func):
        self.func = func
​
    def __call__(self, *args):
        return self[args]
​
    def __missing__(self, key):
        self[key] = self.func(*key)
        return self[key]
​
​
@memoize
def fib(n):
    if n in [0, 1]:
        return n
    return fib(n-1) + fib(n-2)
​
​
if __name__ == '__main__':
    print fib(50)
    print fib(100)


"""
short_list = range(10)
wrapped = wrapper(F, short_list)
print (timeit.timeit(wrapped, number = 1000))

long_list = range(100)
wrapped = wrapper(F, long_list)
print (timeit.timeit(wrapped, number = 10000))
"""



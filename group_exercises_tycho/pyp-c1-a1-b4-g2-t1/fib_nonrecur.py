# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55


fib_list = [0,1] #, 1, 2, 3
def fib2(n):
    global fib_list
    
    if n > len(fib_list):
        start = len(fib_list)   # 2
        stop = n                # 5
        
        
        iterations = stop - start # 3
        
        
        for x in xrange(iterations):                #0,1,2
            fib_numb = fib_list[-1] + fib_list[-2]
            fib_list.append(fib_numb)
    
    return fib_list[n - 1]
    
#Testing area    
    
n = 5
print fib2(n)
print fib_list






"""
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55


fib_list = [0,1] #, 1, 2, 3
def fib2(n):
    global fib_list
    
    if n > len(fib_list):
        start = len(fib_list)
        stop = n
        
        
        iterations = stop - start
        
        
        for x in xrange(iterations):
            fib_numb = fib_list[-1] + fib_list[-2]
            fib_list.append(fib_numb)
    
    return fib_list[n-1]
    
    
"""
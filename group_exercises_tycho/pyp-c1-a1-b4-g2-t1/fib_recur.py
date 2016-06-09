# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

def fib1(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

        
        
        
        
#xrange(start, stop [, step])

#p3: range()
        
        
# testing area   
n = 30    
print (fib1(10))
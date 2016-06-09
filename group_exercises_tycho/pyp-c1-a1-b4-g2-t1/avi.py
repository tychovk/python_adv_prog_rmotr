#0 	1 	1 	2 	3 	5 	8 	13 	21 	34

def fib1(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

def fib2(n):
    fib_sequence = []
    for i in range(n+1):
        if len(fib_sequence) == 0: fib_sequence.append(0)
        elif len(fib_sequence) == 1 or len(fib_sequence) == 2: fib_sequence.append(1)
        else: fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[-1]

def main():
    n_value = int(raw_input("Input n value:"))
    method = raw_input("Solve with recursion (T/F)").upper()
    if method == "T":
        print fib1(n_value)
    else:
        print fib2(n_value)

main()






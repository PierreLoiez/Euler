

def fibbonnacciTillN(n):
    fib = [1]
    fib0, fib1 = 1, 1
    while fib1<n:
        fib.append(fib1)
        fib0, fib1 = fib1, fib0+fib1
        
    return fib

def fibbonacciTillNDigs(n):
    fib = [1]
    fib0, fib1 = 1, 1
    while len(str(fib1))<n:
        fib.append(fib1)
        fib0, fib1 = fib1, fib0+fib1
    fib.append(fib1)
    return fib
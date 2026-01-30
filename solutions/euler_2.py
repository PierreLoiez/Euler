

def Euler2():
    fib0 = 1
    fib1 = 1
    total = 0
    while fib1<4*10**6:
        fib0, fib1 = fib1, fib0+fib1
        if fib1%2==0 and fib1<4*10**6:
            total+=fib1
    return total

print(Euler2())
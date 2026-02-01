import time
from scripts.primes import isPrime, primesUntilN


def nToBase(base, n):
    if n == 0:
        return 0
    inBaseB = ''
    while n>0:
        inBaseB += str(n%base)
        n = n//base
    return int(inBaseB[::-1])

def isPal(n):
    return str(n) == str(n)[::-1]

def Euler36():
    total = 0
    for i in range(10**6):
        if isPal(i):
            iBin = nToBase(2, i)
            if isPal(iBin):
                total += i
    return total
    


start = time.time()
print(Euler36())
print(f'Took {time.time()-start}s')
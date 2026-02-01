
import itertools
import time
from scripts.primes import primesUntilN
from math import *

def maxNForPoly(a, b, primes, biggestVal):
    n = 0
    coef = 0
    while True:
        p1 = n**2 + a*n + b
        for p in primes:
            if p1%p == 0:
                return n, primes, biggestVal
            if p1<=1:
                return n, primes, biggestVal
            if p>sqrt(p1):
                break
        if p1>biggestVal:
            biggestVal = biggestVal*2
            primes = primesUntilN(2*biggestVal)
            print(f'Primes now go till {biggestVal}, a={a}, b={b}')
        n +=1
            

def Euler27():
    biggestVal = 1000
    primes = primesUntilN(biggestVal)
    best = 0
    bestProd = 0
    for a, b in itertools.product(range(1000), range(1001)):
        n1, primes, biggestVal = maxNForPoly(a, b, primes, biggestVal)
        n2, primes, biggestVal = maxNForPoly(-a, b, primes, biggestVal)
        if n1>best:
            print(n1, a, b)
            best = n1
            bestProd = a*b
        if n2>best:
            print(n2, -a, b)
            best = n2
            bestProd = -a*b

    return best, bestProd

start = time.time()
print(Euler27())
print(f'Took {time.time()-start}s')

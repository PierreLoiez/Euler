import time
import itertools
from scripts.primes import isPrime, primesUntilN

from math import *

def rotationsOf(n):
    strN = str(n)
    return [int(strN[s:] + strN[:s]) for s in range(len(strN))]

def Euler35():
    n = 0
    primes = primesUntilN(10**6)
    checked = []
    for p in primes:
        if p not in checked:
            r = rotationsOf(p)
            if all(isPrime(p1, primes) for p1 in r):
                print(p, r)
                n += len(set(r))
                checked += r
    return n
                    


start = time.time()
print(Euler35())
print(f'Took {time.time()-start}s')
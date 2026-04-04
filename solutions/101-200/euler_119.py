import time
from math import *
from scripts.primes import isPrime, primesUntilN
from itertools import permutations

def isInSequence(n, p):
    return sum(int(dig) for dig in str(n))**p == n
            

def Euler119():
    an = []
    n0 = 2
    while len(an)<59:
        for p in range(2, 15):
            n = n0**p
            if isInSequence(n, p):
                an.append(n)
                print(len(an))
                
        n0 += 1
    print(sorted(an))
    return sorted(an)[1], sorted(an)[9], sorted(an)[29]


start = time.time()
print(Euler119())
print(f'Took {time.time()-start}s')
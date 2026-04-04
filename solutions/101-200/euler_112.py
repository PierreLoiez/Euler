import time
from math import *
from scripts.primes import isPrime, primesUntilN
from itertools import permutations


def isIncreasing(n):
    return all(int(str(n)[i])>= int(str(n)[i-1]) for i in range(1, len(str(n))))

def isDecreasing(n):
    return all(int(str(n)[i])<= int(str(n)[i-1]) for i in range(1, len(str(n))))

def isBouncy(n):
    
    return not (isIncreasing(n) or isDecreasing(n))

def Euler112():
    n_bouncy = 0
    n = 0
    threshold = 0.99
    n_inc, n_dec = 0, 0
    while True:
        n += 1
        n_bouncy += isBouncy(n)
        n_inc += isIncreasing(n)
        n_dec += isDecreasing(n)
        if n == 999:
            print(n_inc, n_dec, n-n_bouncy, n_inc+n_dec - (n-n_bouncy))
            break
        if n_bouncy>0:
            if n_bouncy/n == threshold:
                return n


start = time.time()
print(Euler112())
print(f'Took {time.time()-start}s')
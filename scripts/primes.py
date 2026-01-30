from math import *


def primesUntilN(n_final:int):
    n = 3
    primes = [2]
    while n < n_final:
        add2primes = True
        for p in primes:
            if p > sqrt(n):
                break
            if n%p==0:
                add2primes = False
                break
        if add2primes:
            primes.append(n)
    return primes


def primesUntilLen(i_final:int):
    n = 3
    primes = [2]
    while len(primes) < i_final:
        add2primes = True
        for p in primes:
            if p > sqrt(n):
                break
            if n%p==0:
                add2primes = False
                break
        if add2primes:
            primes.append(n)
    
    return primes
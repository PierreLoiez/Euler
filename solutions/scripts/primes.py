from math import *


def primesUntilN(n_final:int):
    primes = [2]
    for n in range(3, n_final, 2):
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
        n +=2
    return primes

def isPrime(n, primes=None):
    if n == 1:
        return False
    if primes is None:
        primes = [2]
        primes = primesUntilN(int(sqrt(n)))
    if sqrt(n)>primes[-1]:
        primes = primesUntilN(int(sqrt(n)))
    for p in primes:
        if p == n:
            return True
        if p>sqrt(n)+1:
            return True
        if n%p == 0:
            return False
    
import time
from math import *
from scripts.divisors import distPrimeFact
from scripts.primes import primesUntilN

def phi(n, primes):
    primeFacts = distPrimeFact(n, primes, {})
    phiN = 1
    for factor, power in primeFacts.items():
        # Using Euler's formula
        phiN = phiN * factor**(power-1) * (factor-1)
    return phiN

def Euler69():
    biggestRatio = 0
    primes = primesUntilN(10**6)
    biggestN = 0
    for n in range(2, 10**6+1):
        phiN = phi(n, primes)
        if n/phiN > biggestRatio:
            biggestRatio = n/phiN
            biggestN = n
    return biggestN


start = time.time()
print(Euler69())
print(f'Took {time.time()-start}s')
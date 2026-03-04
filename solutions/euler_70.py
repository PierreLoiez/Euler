import time
from math import *
from scripts.divisors import distPrimeFact
from scripts.primes import primesUntilN
import tqdm

def phi(n, primes):
    primeFacts = distPrimeFact(n, primes, {})
    phiN = 1
    for factor, power in primeFacts.items():
        # Using Euler's formula
        phiN = phiN * factor**(power-1) * (factor-1)
    return phiN

def isPermOf(n1, n2):
    n1L = sorted(list(str(n1)))
    n2L = sorted(list(str(n2)))
    return n1L == n2L

def Euler70():
    smallestRatio = 10**7
    primes = primesUntilN(10**6)
    smallestN = 0
    for n in tqdm.tqdm(range(2, 10**7+1)):
        phiN = phi(n, primes)
        if n/phiN < smallestRatio and isPermOf(n, phiN):
            smallestRatio = n/phiN
            smallestN = n
    return smallestN


start = time.time()
print(Euler70())
print(f'Took {time.time()-start}s')
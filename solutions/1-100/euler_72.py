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

def Euler72():
    total = 0
    primes = primesUntilN(10**4)
    for d in range(2, 10**6+1):
        nProperFracs = phi(d, primes)
        # Phi gives us the number of numerators that compose the reduced proper fractions of denominator d
        total += nProperFracs
    return total

start = time.time()
print(Euler72())
print(f'Took {time.time()-start}s')
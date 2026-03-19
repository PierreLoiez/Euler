from math import *
import time
from scripts.primes import primesUntilN, isPrime
from scripts.divisors import distPrimeFact
import numpy as np
from scipy.special import gamma
# Link : https://projecteuler.net/problem=18i

def R(p):
    P = np.polynomial.Polynomial([4, -3, 0, 1])
    P2 = np.polynomial.Polynomial([4, p-3, 0, 1])
    product = 1
    product1 = 1
    for i in range(p):
        product = (P(i)*product)
        product1 = (P2(i)*product1)
    return product%p

def EulerB2(): 
    primes = primesUntilN(100)
    P = np.polynomial.Polynomial([4, -3, 0, 1])
    z, nz = [], []
    r1, r2, r3 = P.roots()
    t = 4
    for p in primes:
        print(gamma(p+r1)/gamma(r1)*gamma(p+r2)/gamma(r2)*gamma(p+r3)/gamma(r3))
        print(round(abs(gamma(p+r1)/gamma(r1)*gamma(p+r2)/gamma(r2)*gamma(p+r3)/gamma(r3)))%p, R(p))
    print(z)
    print(nz)

start = time.time()
print(EulerB2())
print(f'Took {time.time()-start}s')

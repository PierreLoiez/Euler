import time
from math import *
from scripts.primes import primesUntilN


def Euler86():
    primes = primesUntilN(10000)
    limit = 50*10**6
    sumOfPPowers = {}
    for p1 in primes:
        for p2 in primes:
            for p3 in primes:
                total = p1**2 + p2**3 + p3**4
                if total > limit:
                    break
                sumOfPPowers[total] = sumOfPPowers.get(total, []) + [[p1, p2, p3]]
            if p2**3 + p1**2 > limit:
                break
        if p1 ** 2>limit:
            break
    return len(sumOfPPowers.values())
        
    

start = time.time()
print(Euler86())
print(f'Took {time.time()-start}s')
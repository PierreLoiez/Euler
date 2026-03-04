import time
from math import *
from scripts.divisors import distPrimeFact
from scripts.primes import primesUntilN
import tqdm



def Euler73():
    count = 0
    for d in range(2, 12001):
        for n in range(int(1/3*d), int(1/2*d)+1):
            if 1/3<n/d<1/2 and gcd(n, d) ==1:
                count += 1
    return count

start = time.time()
print(Euler73())
print(f'Took {time.time()-start}s')
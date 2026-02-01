import time
from scripts.primes import *
from scripts.divisors import *


def Euler48():
    total = 0
    for i in range(1, 1001):
        total = (total+i**i)%(10**10)
    return total
        

start = time.time()
print(Euler48())
print(f'Took {time.time()-start}s')
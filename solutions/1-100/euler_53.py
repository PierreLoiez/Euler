import time
from scripts.primes import *
from scripts.divisors import *
from math import *


def Euler53():
    count = 0
    for n in range(1, 101):
        if factorial(n)>10**6:
            r = n//2
            while factorial(n)/(factorial(n-r)*factorial(r))>10**6:
                count += 1 if n%2 == 0 and r == n//2 else 2 
                r -=1
                # Since combinatorics are symmetrical around n/2 but if n is even that intervenes only once                r -= 1
    return count

start = time.time()
print(Euler53())
print(f'Took {time.time()-start}s')
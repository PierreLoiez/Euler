import time
from scripts.primes import *
from scripts.divisors import *
from math import *

def sumOfDigs(n):
    strN = str(n)

    return sum(int(d) for d in strN)
        
def Euler56():
    best = 0
    for a in range(2, 100):
        for b in range(1, 100):
            n = a**b
            if n>10**20:
                print(n)
            totalOfDigs = sumOfDigs(n)
            if totalOfDigs>best:
                best = totalOfDigs
    return best
    

start = time.time()
print(Euler56())
print(f'Took {time.time()-start}s')
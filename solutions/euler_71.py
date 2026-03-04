import time
from math import *
from scripts.divisors import distPrimeFact
from scripts.primes import primesUntilN
import tqdm



def Euler71():
    three7ths = 3/7
    closest = 1
    closestN = 0
    for d in range(2, 10**6+1):
        n = int(3/7*d)
        # the key of the problem is to start at the right place. int() gives the floor of the float put in, so the closest 
        # approximation is the one done here
        while n/d<three7ths:
            if three7ths - n/d < closest:
                closest = three7ths - n/d 
                closestN = n
            n += 1
    return closestN

start = time.time()
print(Euler71())
print(f'Took {time.time()-start}s')
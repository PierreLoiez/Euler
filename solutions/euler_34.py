import time
import itertools

from math import *

def Euler34():
    maxN = factorial(9) * len(str(factorial(9)))
    total = 0
    for i in range(3, maxN):
        sumFDigs = sum(factorial(int(d)) for d in str(i))
        if sumFDigs == i:
            total += i
    return total


start = time.time()
print(Euler34())
print(f'Took {time.time()-start}s')
import time
from math import *
from scripts.primes import isPrime, primesUntilN
from itertools import permutations


def Euler120():
    maxes = {a:0 for a in range(3, 1001)}
    
    for a in range(3, 1001):
        t1_poss, t2_poss = [], []
        n = 1
        t1, t2 = ((a+1)**n)%(a**2), ((a-1)**n)%(a**2)
        while t1 not in t1_poss or t2 not in t2_poss:
            t1_poss.append(t1)
            t2_poss.append(t2)
            n += 1
            t1, t2 = ((a+1)**n)%(a**2), ((a-1)**n)%(a**2)
        for i in range(n-1):
            term = (t1_poss[i] + t2_poss[i])%a**2
            maxes[a] = max(term, maxes[a])
    print(maxes[7])
    return sum(maxes.values())
        
    


start = time.time()
print(Euler120())
print(f'Took {time.time()-start}s')
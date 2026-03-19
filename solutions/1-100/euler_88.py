import time
from math import *
from scripts.divisors import properDivisorsOf
from scripts.primes import primesUntilN

def getMinK(n, prod, sum, depth = 1, minFact = 2):
    result = 0
    if prod == 1:
        return valid(n, depth + sum - 1)
    if prod == sum and depth>1:
        return valid(n, depth)
    elif depth>1 and valid(n, depth+sum-prod):
        result += 1
    divisors = properDivisorsOf(prod)
    divisors.sort()
    divisors = [d for d in divisors if d>=minFact]
    for d in divisors:
        result += getMinK(n, prod//d, sum-d, depth+1, minFact=d)
    return result
def valid(n, k):
    global minKs, maxK, limit
    if k>limit:
        return 0
    if minKs[k]>n:
        minKs[k] = n
        return 1
    return 0

def Euler88():
    global minKs, maxK, limit
    maxK = 0
    limit = 12000
    minKs = [10**10 for _ in range(12001)]
    sols = []
    n = 2
    need2find = limit-1
    while need2find>0:
        applicable = getMinK(n, n, n)
        if applicable != 0:
            print(n, applicable, maxK)
            need2find -= applicable
            sols.append(n)
        n += 1
    return sum(sols)

start = time.time()
print(Euler88())
print(f'Took {time.time()-start}s')
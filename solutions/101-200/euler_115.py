import time
from math import *
from scripts.primes import isPrime, primesUntilN
from itertools import permutations

def countWays(n, m=3):
    global blockArrangements
    if n==0:
        return 1
    try:
        return blockArrangements[(n, m)]
    except KeyError:
        pass
    toRet = countWays(n-1, m)
    for blockSize in range(m, n+1):
        nextBlock = n-blockSize
        if nextBlock>0:
            nextBlock -= 1
        toRet += countWays(nextBlock, m)
    
    blockArrangements[(n, m)] = toRet
    return toRet

def Euler115():
    global blockArrangements
    blockArrangements = {}
    n = 50
    while countWays(n, 50)<10**6:
        n += 1
    return n



start = time.time()
print(Euler115())
print(f'Took {time.time()-start}s')
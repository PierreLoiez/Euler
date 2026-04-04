import contextlib
import time
from math import *
from scripts.primes import isPrime, primesUntilN
from itertools import permutations

def countWays(n, m=3):
    global blockArrangements
    if n==0:
        return 1
    with contextlib.suppress(KeyError):
        return blockArrangements[(n, m)]
    toRet = countWays(n-1, m)
    for blockSize in range(m, n+1):
        nextBlock = n-blockSize
        if nextBlock>0:
            nextBlock -= 1
        toRet += countWays(nextBlock, m)

    blockArrangements[(n, m)] = toRet
    return toRet

def Euler114():
    global blockArrangements
    blockArrangements = {}
    return countWays(50, 3)



start = time.time()
print(Euler114())
print(f'Took {time.time()-start}s')
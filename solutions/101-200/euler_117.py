import contextlib
import time
from math import *
from scripts.primes import isPrime, primesUntilN
from itertools import permutations

def countWays(n, m=3):
    global blockArrangements
    options = [2, 3, 4]
    if n==0:
        return 1
    with contextlib.suppress(KeyError):
        return blockArrangements[(n, m)]
    toRet = countWays(n-1, m)
    for blockSize in options:
        nextBlock = n-blockSize
        if nextBlock<0:
            continue
        toRet += countWays(nextBlock, m)

    blockArrangements[(n, m)] = toRet
    return toRet

def Euler117():
    global blockArrangements
    blockArrangements = {}
    n = 50
    return countWays(n, 2)



start = time.time()
print(Euler117())
print(f'Took {time.time()-start}s')
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
    for blockSize in range(m, m+1):
        nextBlock = n-blockSize
        if nextBlock<0:
            continue
        toRet += countWays(nextBlock, m)

    blockArrangements[(n, m)] = toRet
    return toRet

def Euler116():
    global blockArrangements
    blockArrangements = {}
    n = 50
    print(countWays(n, 2), countWays(n, 3), countWays(n, 4))
    print(blockArrangements)
    return countWays(n, 2) + countWays(n, 3) + countWays(n, 4) -3



start = time.time()
print(Euler116())
print(f'Took {time.time()-start}s')
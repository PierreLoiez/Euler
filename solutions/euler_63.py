import time
from scripts.primes import primesUntilLen, isPrime
import itertools



def Euler63():
    length = 1
    count = 0
    while len(str(9**length))==length:
        print(length)
        base = 1
        baseToPower = base**length
        while len(str(baseToPower))<=length:
            if len(str(baseToPower)) == length:
                count += 1
            base += 1
            baseToPower = base**length
        length += 1
    return count

start = time.time()
print(Euler63())
print(f'Took {time.time()-start}s')
import time
from scripts.primes import *
from scripts.divisors import *
import itertools


def Euler51():
    primes = primesUntilN(1000000)
    possibilities = '0123456789*' # Use the stars to represent the digits that will be replaced
    end = '1379'
    for ds in itertools.product(possibilities, possibilities, possibilities, possibilities, possibilities, possibilities, possibilities, end):
        # Prime numbers end in either 3, 1, 7 or 9, so restricted the last digit that way
        if '*' not in ds:
            continue
        num = ''.join(ds)
        count = 0
        startsWithStar = len(str(int(num.replace('*', '1')))) == len(str(int(num.replace('*', '0')))) 
        # Check that a star is not at the beginning of the number (if it is, we cannot try 0)
        loopTill = -1 if startsWithStar else 0
        for i in range(9, loopTill, -1):
            n = int(num.replace('*', str(i))) 
            if isPrime(n, primes):
                count +=1
            if count == 8:
                return n

start = time.time()
print(Euler51())
print(f'Took {time.time()-start}s')
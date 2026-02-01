import time
from scripts.primes import *



def Euler46():
    primes = primesUntilN(100000)
    for i in range(1, 50000):
        n = 2*i+1
        if not isPrime(n, primes):
            for p in primes:
                if p>n:
                    return n
                if sqrt((n-p)/2)%1 == 0:
                    break
            

start = time.time()
print(Euler46())
print(f'Took {time.time()-start}s')
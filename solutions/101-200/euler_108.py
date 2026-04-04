import time
from math import *
from scripts.primes import isPrime, primesUntilN



def nDivisorsOf(n, biggestPrime):
    divs = []
    global primes
    n0 = n
    primeDecomp = {}
    while n0 != 1:
        
        for p in primes:
            if p>biggestPrime:
                return 0
            if n0%p==0:
                primeDecomp[p] = 0
            while n0%p==0:
                n0 = n0//p
                primeDecomp[p] += 1
            if p>= sqrt(n0):
                break
    
    return (prod(i+1 for i in primeDecomp.values())+1)//2


def Euler108():
    n = 3
    maximum=0
    global primes
    start = time.time()
    primes = primesUntilN(100)
    biggestPrime = primes[int(log2(1000))+1]
    em, ms = 0, 0
    while True:
        nb = nDivisorsOf(n**2, biggestPrime)
        try:
            if nb>maximum:
                print(n, nb, time.time() - start)
                maximum = nb
                if nb>= 1000:  
                    return n
                
        except ValueError:
            pass
        # input(n)
        n += 1
        


start = time.time()
print(Euler108())
print(f'Took {time.time()-start}s')
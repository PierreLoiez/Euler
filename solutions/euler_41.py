import time
from math import *
from scripts.primes import *

def lexicoPerm(base, n):
    newOrder = ''
    for i in range(len(base)-1, -1, -1):
        newOrder += base[min(n//factorial(i), i)]
        base=base.replace(base[min(n//factorial(i), i)], '')
        n = n%factorial(i)
    return newOrder


def Euler41():
    allDigs = '123456789'
    best = 0
    primes = primesUntilN(100000)
    for n in range(9, 0, -1):
        print(n)
        digsN = allDigs[:n+1][::-1]
        for i in range(factorial(n+1)):
            newOrder = lexicoPerm(digsN, i)
            if isPrime(int(newOrder), primes):
                return newOrder


start = time.time()
print(Euler41())
print(f'Took {time.time()-start}s')
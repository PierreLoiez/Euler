import time
from scripts.primes import isPrime, primesUntilN


def isPanDig(n):
    digs = '123456879'
    return all(d in str(n) for d in digs)

def Euler38():
    best = 0
    for n in range(1, 10000):
        concatMults = ''
        i=1
        while len(concatMults)<9:
            concatMults += str(i*n)
            i += 1
        if len(concatMults)==9 and isPanDig(concatMults) and int(concatMults) > best:
            best = int(concatMults)
    return best


start = time.time()
print(Euler38())
print(f'Took {time.time()-start}s')
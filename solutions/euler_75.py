import time
from math import *
from scripts.divisors import distPrimeFact
from scripts.primes import primesUntilN
import tqdm

def getTripleFrom(s, t):
    return [s**2-t**2, 2*s*t, s**2+t**2]
    

def Euler75():
    s = 2
    global Lmax
    Lmax = 15*10**5
    primeTriangles = []
    s = 2
    t = 1
    triple = getTripleFrom(s, t)
    L = sum(triple)
    while L<Lmax:
        
        while L<=Lmax and t<s:
            if gcd(triple[0], triple[1], triple[2]) == 1:
                primeTriangles.append(triple)
            t += 1
            triple = getTripleFrom(s, t)
            L = sum(triple)
        
        s += 1
        t = 1
        triple = getTripleFrom(s, t)
        L = sum(triple)
        
    trianglesOfLen = {}
    for t in primeTriangles:
        k = 1
        L = sum(t)
        while L<Lmax:
            n = trianglesOfLen.get(L, 0) + 1
            trianglesOfLen[L] = n
            k += 1
            L = sum(t)*k
        
    return list(trianglesOfLen.values()).count(1)

start = time.time()
print(Euler75())
print(f'Took {time.time()-start}s')
import time
from math import *


def getTripleFrom(s, t):
    return [s**2-t**2, 2*s*t, s**2+t**2]

def sumOfValues(dictionary, maxValue = None):
    if maxValue is None:
        return sum(list(dictionary.values()))
    else:
        return sum(v for k, v in dictionary.items() if k < maxValue)

def Euler87():
    cubesOfM = {i:0 for i in range(3, 10001)}
    primeTriples = []
    for s in range(2, 101):
        for t in range(1, s):
            [a, b, c] = getTripleFrom(s, t)
            if gcd(a, b, c) == 1:
                primeTriples.append([a, b])
    print(primeTriples)
    allTriples = []
    for triple in primeTriples:
        [a, b] = triple
        d = 1
        while min(a*d, b*d)<10000:
            if a*d<10000:
                allTriples.append([a*d, b*d])
            if b*d<10000:
                allTriples.append([b*d, a*d])
            d += 1
    print(f'Got the triples! {len(allTriples)}')
    for triple in allTriples:
        [s1, b] = triple
        if b//2 > s1:
            continue
        for i in range(1, b//2+1):
            s2, s3 = i, b-i
            if s2>s1 or s3>s1:
                continue
            cubesOfM[s1] += 1
    print(sumOfValues(cubesOfM, 101))
    for i in range(3, 10001):
        if sumOfValues(cubesOfM, i+1) >10**6:
            return i
        
    

start = time.time()
print(Euler87())
print(f'Took {time.time()-start}s')
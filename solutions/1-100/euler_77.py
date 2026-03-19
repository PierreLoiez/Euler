import time
from math import *
from scripts.primes import primesUntilLen, isPrime


def getBreakdowns(n, breakdownsOf):
    newBreakdowns = []
    breakdowns = []
    for p in primes:
        if p>n//2:
            break
        breakdown = {p:1}
        breakdown[n-p] = breakdown.get(n-p, 0)+1
        if len(breakdownsOf[n-p])>0:
            newBreakdowns.append(breakdown)
        if isPrime(n-p, primes):
            breakdowns.append(breakdown)
    for b in newBreakdowns:
        for key, value in b.items():
            if len(b.keys())>1:
                if not isPrime(list(b.keys())[(list(b.keys()).index(key)+1)%2], primes):
                    continue
            base = b.copy()
            if value == 1:
                base.pop(key)
            else:
                base[key] -= 1
            for oldBd in breakdownsOf[key]:
                breakdown = base.copy()
                for k, v in oldBd.items():
                    breakdown[k] = v + breakdown.get(k, 0)
                if breakdown not in breakdowns:
                    breakdowns.append(breakdown)
    return breakdowns

def Euler77():
    global primes
    primes = primesUntilLen(10000)
    breakdownsOf = {1:[], 2:[], 3:[]}
    n = 4
    while len(breakdownsOf[n-1])<5000:
        breakdownsOf[n] = getBreakdowns(n, breakdownsOf)
        n += 1
    return n-1
        
start = time.time()
print(Euler77())
print(f'Took {time.time()-start}s')
import time
from scripts.primes import *
from scripts.divisors import *

def permutations(n):
    
    perms = []
    base = str(n)
    for a in base:
        base0 = base.replace(a, '', 1)
        for b in base0:
            base1 = base0.replace(b, '', 1)
            perms.extend(int(a+b+c + base1.replace(c, '', 1)) for c in base1)
    return list(set(perms))

def Euler50():
    primes = primesUntilN(1000000)
    results = {}
    for i in range(len(primes)):
        total = 0
        n=0
        for p in primes[i:]:
            total += p
            n += 1
            if total > 10**6:
                break
            if isPrime(total, primes):
                results[n] = total
    maxN = max(list(results.keys()))
    return results[maxN]

start = time.time()
print(Euler50())
print(f'Took {time.time()-start}s')
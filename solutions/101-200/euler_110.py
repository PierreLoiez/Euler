import time
from math import *
from scripts.primes import isPrime, primesUntilN



def value(decomp):
    return prod(prime**power for prime, power in decomp.items())

def n_decomps(decomp):
    return (prod((2*i+1) for i in decomp.values())+1)//2

def condense(decomp, smallestInd = 0):
    global mini, maxInd, primes
    # print(decomp, n_decomps(decomp))
    if smallestInd > 0: # Cannot be a valid answer if we skip a prime factor
        if min(list(decomp.values())[:smallestInd])<list(decomp.values())[smallestInd]:
            return None
    if value(decomp) > mini: # No point iterating further down a branch that is bigger than a valid answer
        return None
    if n_decomps(decomp) >=limit: 
        mini = min(mini, value(decomp))
        print(mini, decomp)
        return None
    for p in range(smallestInd, maxInd):
        # Recursively check all possible options, the invalid ones will be skipped automatically
        copy = decomp.copy()
        copy[primes[p]] += 1
        condense(copy, p)

def Euler110():
    global primes, mini, maxInd, limit
    limit = 4000000
    primes = primesUntilN(200)
    maxInd = int(log(limit*2, 3)) +1 # The number of prime factors for n**2 to have 4000000 factors 
    mini = prod(primes[:maxInd]) # Corresponding value
    base = {p:0 for p in primes[:maxInd]} # We start with 1
    
    condense(base)
    return mini


start = time.time()
print(Euler110())
print(f'Took {time.time()-start}s')
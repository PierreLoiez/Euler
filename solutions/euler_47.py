import time
from scripts.primes import *
from scripts.divisors import *


def Euler47():
    primes = primesUntilN(1000000)
    n = 3
    best = 0
    while best < 4:
        if len(distPrimeFact(n, primes, {}).keys()) == 4:
            if len(distPrimeFact(n+1, primes, {}).keys())==4:
                if len(distPrimeFact(n+2, primes, {}).keys())==4:
                    
                    if len(distPrimeFact(n+3, primes, {}).keys())==4:
                        
                        return n
                    else:
                        n += 4
                else:
                    n+=3
            else:
                n += 2
        else:
            n+=1
            

start = time.time()
print(Euler47())
print(f'Took {time.time()-start}s')
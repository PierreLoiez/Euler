import time
from math import *
from scripts.primes import isPrime, primesUntilN
from itertools import permutations



def Euler111():
    n = 10
    global primes
    primes = primesUntilN(int(10**((n+1)/2))+1)
    s = 0
    for d in range(10):
        for m in range(n, 0, -1):
            found = False
            perms = set(permutations(list(str(d)*m + 'p'*(n-m)), n))
            for p in range(10**(n-m)):
                for perm in perms:
                    strings = ''.join(perm).split('p')
                    toRep = '0'*(n-m-len(str(p))) + str(p)
                    string = ''.join(strings[i] + toRep[i] for i in range(n-m))
                    string += strings[-1]
                    number = int(string)
                    if len(str(number)) == n and isPrime(number, primes):
                        s += number
                        found = True
            if found:
                break
    return s



start = time.time()
print(Euler111())
print(f'Took {time.time()-start}s')
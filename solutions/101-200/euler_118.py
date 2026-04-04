import time
from math import *
from scripts.primes import isPrime, primesUntilN
from itertools import permutations

def checkPermutation(perm, history=None, listONums=None):
    if history is None:
        history = []
    if listONums is None:
        listONums = []
    global primes, checked
    history = perm if len(history) == 0 else history
    if len(perm) == 0 and checked.get(tuple(sorted(listONums)), True):
        checked[tuple(sorted(listONums))] = False
        return None
    for i in range(1,len(perm)+1):
        n = int(perm[:i])
        if isPrime(n, primes):
            checkPermutation(perm[i:], history, listONums+[n])

    
        

def Euler118():
    global primes, checked
    checked = {}
    primes = primesUntilN(10**5)
    perms = list(permutations(list('123456789'), 9))
    for perm in perms:
        #print(perm)
        string = ''.join(perm)
        checkPermutation(string)
    return len(checked.values())



start = time.time()
print(Euler118())
print(f'Took {time.time()-start}s')
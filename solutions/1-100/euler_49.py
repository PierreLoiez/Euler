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

def Euler48():
    primes = primesUntilN(1000)
    checked = {}
    for i in range(1000, 10000):
        if checked.get(i, 0)==0:
            permsI = permutations(i)
            for p in permsI:
                checked[p] = 1
            permsI = [p for p in permsI if p>999 and isPrime(p, primes)]
            permsI.sort()
            if len(permsI)>= 3:
                for j in range(len(permsI)-2):
                    firstTerm = permsI[j]
                    for secondTerm in permsI[j+1:-1]:
                        d = secondTerm-firstTerm
                        thirdTerm = d+secondTerm
                        if thirdTerm in permsI:
                            print(firstTerm, secondTerm, thirdTerm)

start = time.time()
print(Euler48())
print(f'Took {time.time()-start}s')
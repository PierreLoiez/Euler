import time
from math import *
from scripts.divisors import properDivisorsOf

    

def amicableChain(n_0):
    global checked
    n = n_0
    chain = [n]
    while checked.get(n, True):
        checked[n] = False
        n = sum(properDivisorsOf(n))
        chain.append(n)
        if n>10**6:
            return []
    return list(set(chain[chain.index(n):])) if n in chain else []

def Euler95():
    global checked
    best = []
    checked = {1:False}
    for i in range(2,10**6):
        chain = amicableChain(i)
        if len(chain)> len(best):
            best = chain
    return min(best)

start = time.time()
print(Euler95())
print(f'Took {time.time()-start}s')
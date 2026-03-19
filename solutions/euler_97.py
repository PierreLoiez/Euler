import itertools
import time
from math import *
from scripts.divisors import properDivisorsOf



def Euler97():
    base = 28433*2**(7830457%4)
    for _ in range(7830457//4):
        base = (base*2**4)%10**10
    return base+1

start = time.time()
print(Euler97())
print(f'Took {time.time()-start}s')
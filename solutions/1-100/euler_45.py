import time
from math import *
import itertools

def checkHTP(h):
    n_t = -0.5+sqrt(0.5**2+4*0.5*h)
    n_p = (0.5+sqrt(0.5**2+4*1.5*h))/3
    return n_t%1==0 and n_p%1==0

def Euler45():
    n = 144
    while True:
        h = n*(2*n-1)
        if checkHTP(h):
            return h
        n += 1

start = time.time()
print(Euler45())
print(f'Took {time.time()-start}s')
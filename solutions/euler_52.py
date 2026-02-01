import time
from scripts.primes import *
from scripts.divisors import *
import itertools


def Euler52():
    i = 1
    while True:
        strIs = [list(str(i)), list(str(i*2)), list(str(i*3)), list(str(i*4)), list(str(i*5)), list(str(i*6))]
        if len(strIs[5]) > len(strIs[0]):
            i = 2*i
            continue
        standard = strIs[0]
        standard.sort()
        retI = True
        for other in strIs:
            other.sort()
            if other != standard:
                retI = False
                break
        if retI:
            return i
        i += 1
    

start = time.time()
print(Euler52())
print(f'Took {time.time()-start}s')
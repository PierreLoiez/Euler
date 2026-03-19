import time
from math import *
import itertools

    
def findEnd(n):
    while n not in [1, 89]:
        n = sum(int(i)**2 for i in str(n))
    return n

def Euler92():
    return sum(findEnd(n) == 89 for n in range(1,10**7))

start = time.time()
print(Euler92())
print(f'Took {time.time()-start}s')
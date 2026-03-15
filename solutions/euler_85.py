import itertools
import random
import time
from math import *
import numpy as np

def numberOfRectangles(s1, s2):
    return sum(
        (s1 - minis1) * (s2 - minis2)
        for minis1, minis2 in itertools.product(range(s1), range(s2))
    )

def Euler85():
    closest = 0
    closestN = None
    for s1 in range(1, 2000):
        for s2 in range(1, s1):
            nRects = numberOfRectangles(s1, s2)
            if abs(nRects-2*10**6)<abs(closest-2*10**6):
                closest=nRects
                closestN = (s1, s2)
            if nRects>2*10**6:
                break
    
    
    return closestN[0]*closestN[1]
    

start = time.time()
print(Euler85())
print(f'Took {time.time()-start}s')
import time
from math import *
import itertools

    
def isRAngleT(x1, x2, y1, y2):
    if (x1,y1) == (x2,y2) or (x1,y1) == (0,0) or (x2,y2) == (0,0):
        return False
    sides = [x1**2+y1**2, x2**2+y2**2, (x1-x2)**2 + (y1-y2)**2]
    sides.sort()
    a, b, c = sides
    return a+b==c

def Euler91():
    limits = 50
    N = sum(bool(isRAngleT(x1, x2, y1, y2))
        for x1, x2, y1, y2 in itertools.product(
                    range(limits + 1),
                    range(limits + 1),
                    range(limits + 1),
                    range(limits + 1),
                ))
    return N/2
            

start = time.time()
print(Euler91())
print(f'Took {time.time()-start}s')
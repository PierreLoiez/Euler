import time
from math import *

def isPerfectTriangle(a, b):
    return sqrt(a**2+b**2)%1 == 0


def Euler39():
    triangles = {i:[] for i in range(1,1001)}
    for a in range(1, 1000):
        for b in range(a, 1000):
            c = sqrt(a**2+b**2)
            if a+b+c<=1000:
                if c%1==0:
                    triangles[a+b+c].append((a, b, c))
            else:
                break
    best = 0
    bestP = 0
    print(triangles)
    for p in range(1, 1001):
        if len(triangles[p])>best:
            best = len(triangles[p])
            bestP = p
    return best, bestP

start = time.time()
print(Euler39())
print(f'Took {time.time()-start}s')
import time
from math import *
import itertools



def Euler44():
    i = 1
    pentagonals = [int(i*(i*3-1)/2) for i in range(1, 3000)]
    while True:
        print(i)
        p1 = pentagonals[i]
        for j in range(i, -1, -1):
            p2 = pentagonals[j]
            sigma = p1+p2
            if sigma>pentagonals[-1]:
                pentagonals += [int(i*(i*3-1)/2) for i in range(len(pentagonals), 3*len(pentagonals))]
            delta = p1-p2
            if sigma in pentagonals and delta in pentagonals:
                return delta
        i += 1
    

start = time.time()
print(Euler44())
print(f'Took {time.time()-start}s')
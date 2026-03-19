import time
from math import *


def findNumFromSeq(sequence):
    seq = sequence[::-1]
    n = 1
    d = seq[0]
    for s in seq[1:]:
        n = d*s+n
        n, d = d, n
    n, d = d, n
    return n
        

def Euler65():
    total = 0
    sequence = [2]
    for i in range(1, 100):
        if i%3==2:
            sequence.append((i+1)//3*2)
        else:
            sequence.append(1)

    return sum(int(i) for i in str(findNumFromSeq(sequence)))
start = time.time()
print(Euler65())
print(f'Took {time.time()-start}s')
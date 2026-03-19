import time
from math import *

def getNBreakdowns(n):
    for i in range(n//2, 0, -1):
        for j in range(1, i+1):
            n_breakdowns[(n, j)] = n_breakdowns.get((n, j), 0) + 1 + n_breakdowns.get((n-i, i), 0)
    return n_breakdowns[(n, 1)]

def Euler76():
    # A better method exists but this one is good enough for these purposes
    global n_breakdowns
    n_breakdowns = {(2, 1):1}
    for n in range(3, 101):
        getNBreakdowns(n)
    print(n_breakdowns[(74, 1)])
    return n_breakdowns[(100, 1)]

start = time.time()
print(Euler76())
print(f'Took {time.time()-start}s')
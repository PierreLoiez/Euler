import itertools
import pathlib
import time
from math import *
from scripts.divisors import properDivisorsOf


def findSequenceForRoot(N):
    #We recover the 
    rootN = sqrt(N)
    a0 = int(rootN)
    listOfa = [a0]
    ns = [a0]
    ds = [1]
    d = N-ns[-1]**2
    a = int((rootN+a0)/d)
    n = abs(a0-d*a)
    while True:
        ns.append(n)
        ds.append(d)
        listOfa.append(a)
        d1 = n
        n1 = d
        n, d = n1*d1, N - d1**2
        common = gcd(d, n1)
        n, d = n//common, d//common
        a = int((a0+n)/d)
        n = abs(n-a*d)
        if n in ns and ds[ns.index(n)] == d: 
            # Breaks when the same numbers are at the top and bottom of the fraction (it will give the same result)
            break
    if len(listOfa) != 1 or listOfa[0] != a: 
        # Necessary since the check for numerators and denominators is done at the end of the loop but before the new a is added
        listOfa.append(a)
    return listOfa
        

def findNumDenFromSeq(sequence):
    seq = sequence[::-1]
    n = 1
    d = seq[0]
    for s in seq[1:]:
        n = d*s+n
        n, d = d, n
    
    n, d = d, n
    return n, d

def Euler100():
    # A bit of tinkering with the problem's setup gets us that solving this problem is equivalent to looking for solutions of 2*y**2 - x**2 = 1
    # Research on Pell's Equation tells us that we can get the next solution through a recurrence sequence. 
    sequence = findSequenceForRoot(2)
    sequence = sequence + sequence[1:-1][::-1]
    for i in range(1, len(sequence)+1):
        x, y = findNumDenFromSeq(sequence[:i])
        if x**2-2*y**2 == -1:
            break
    x_0, y_0 = x, y
    while x<10**12:
        x_k, y_k = x, y
        x, y = x_0*x_k + 2*y_0*y_k, x_0*y_k + y_0*x_k
    n_b = (y+1)//2
    n_total = (x+1)//2
    return n_b, n_total, (n_total*(n_total-1))%(n_b*(n_b-1))


start = time.time()
print(Euler100())
print(f'Took {time.time()-start}s')
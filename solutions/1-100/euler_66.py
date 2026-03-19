import time
from math import *

# A bit of research shows that Pell's Equation is the easiest way to go about solving this problem

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

def Euler66():
    biggestD = 0
    for n in range(1, 1001):
        if sqrt(n)%1==0:
            continue
        sequence = findSequenceForRoot(n)
        sequence = sequence + sequence[1:len(sequence)-1][::-1]
        for i in range(1, len(sequence)+1):
            x, y = findNumDenFromSeq(sequence[:i])
            if x**2-n*y**2 == 1:
                if abs(x)>biggestD:
                    biggestD = x
                    print(n, x)
                break
            if i == len(sequence):
                print(n, x, y, x**2-n*y**2)
    return biggestD
    
start = time.time()
print(Euler66())
print(f'Took {time.time()-start}s')
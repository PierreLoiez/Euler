import time
from math import *

def findPeriodFor(N):
    rootN = sqrt(N)
    a0 = int(rootN)
    listOfa = []
    ns = [a0]
    ds = [1]
    d = N-ns[-1]**2
    a = int((rootN+a0)/d)
    n = abs(a0-d*a)
    while True:
        #print(n, d, a)
        ns.append(n)
        ds.append(d)
        listOfa.append(a)
        #print(f'Mile 1: n={n}, d={d}, a={a}')
        d1 = n
        n1 = d
        #print(f'Mile 2: n={n1}, d={d1}, a={a}')
        n, d = n1*d1, N - d1**2
        #print(f'Mile 3: n={n}, d={d}, a={a}')
        common = gcd(d, n1)
        n, d = n//common, d//common
        a = int((a0+n)/d)
        n = abs(n-a*d)
        #print(f'Mile 4: n={n}, d={d}, a={a}')
        if n in ns and ds[ns.index(n)] == d: 
            # Breaks when the same numbers are at the top and bottom of the fraction (it will give the same result)
            break
    if len(listOfa) != 1 or listOfa[0] != a: 
        # Necessary since the check for numerators and denominators is done at the end of the loop but before the new a is added
        listOfa.append(a)
    return listOfa


def Euler64():
    count = 0
    for N in range(2, 10001):
        if sqrt(N)%1 == 0:
            continue
        period = findPeriodFor(N)
        print(N, period)
        if len(period)%2==1:
            count += 1
    return count

start = time.time()
print(Euler64())
print(f'Took {time.time()-start}s')
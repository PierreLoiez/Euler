import contextlib
import pathlib
import time
from math import *
from scripts.divisors import properDivisorsOf
from numpy.polynomial import Polynomial
from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def disjoint(S1, S2):
    return all(s not in S2 for s in S1)

def isSpecialSum(A):
    valsByLen = {i:{} for i in range(len(A)+1)}
    subsets = powerset(A)
    for s in subsets:
        sums = sum(s)
        for s1, sums1 in valsByLen[len(s)].items():
            if sums == sums1 and disjoint(s, s1):
                return False
        valsByLen[len(s)][s] = sums
    for l1 in range(1, len(A)):
        for l2 in range(1, l1):
            l1vals = valsByLen[l1].values()
            l2vals = valsByLen[l2].values()
            if min(l1vals)<=max(l2vals):
                return False
    return True


def Euler103():
    A = [11, 12, 13, 14, 15, 16, 17]
    for a in range(17, 100):
        print(a)
        for b in range(16, a):
            if isSpecialSum([a, b]):
                for c in range(15, b):
                    if isSpecialSum([a, b, c]):
                        for d in range(14, c):
                            if isSpecialSum([a, b, c, d]):
                                for e in range(13, d):
                                    if isSpecialSum([a, b, c, d, e]):
                                        for f in range(12, e):
                                            if isSpecialSum([a, b, c, d, e, f]):
                                                for g in range(11, f):
                                                    if isSpecialSum([a, b, c, d, e, f, g]):
                                                        A = [a, b, c, d, e, f, g]
                                                        A.sort()
                                                        print(A, sum(A), ''.join(str(i) for i in A))
                            
    return None
    

start = time.time()
print(Euler103())
print(f'Took {time.time()-start}s')
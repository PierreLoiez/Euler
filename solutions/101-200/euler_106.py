import contextlib
import pathlib
import time
from math import *
from scripts.divisors import properDivisorsOf
from numpy.polynomial import Polynomial
from itertools import chain, combinations
import sys

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

def worthChecking(s1, s2):
    if len(s1) != len(s2) or len(s1) == 1:
        return False
    standard = s1[0] - s2[0]
    return any(standard * (s1[i] - s2[i])<=0 for i in range(1, len(s1)))

def Euler106():
    n = 12
    base = list(range(n))
    sets = list(powerset(base))
    total = 0
    checkedElements = {}
    possiblePairs = 0
    for ind1 in range(len(sets)):
        set1 = sets[ind1]
        for ind2 in range(ind1+1, len(sets)):
            set2 = sets[ind2]
            allElems = tuple(sorted(list(set1) + list(set2)))

            if n>len(set2)>0 and n>len(set1)>0 and disjoint(set1, set2):
                possiblePairs += 1
                if worthChecking(set1, set2):
                    checkedElements[allElems] = True
                    total += 1
    return total, possiblePairs

start = time.time()
print(Euler106())
print(f'Took {time.time()-start}s')
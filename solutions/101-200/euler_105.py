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


def Euler105():
    raw = pathlib.Path('../resources/sets.txt').read_text()
    sets = raw.split('\n')
    total = 0
    for set in sets:
        set = set.split(',')
        intSet = [int(s) for s in set]
        if isSpecialSum(intSet):
            total += sum(intSet)
    return total

start = time.time()
print(Euler105())
print(f'Took {time.time()-start}s')
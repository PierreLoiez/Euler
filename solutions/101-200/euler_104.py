import contextlib
import pathlib
import time
from math import *
from scripts.divisors import properDivisorsOf
from numpy.polynomial import Polynomial
from itertools import chain, combinations
import sys




def Euler104():
    sys.set_int_max_str_digits(100000)
    f0 = 1
    f1=1
    n = 2
    t1 = 0
    t2 = 0
    div = 1
    while True:
        hold = f1
        f1 = f1+f0
        f0 = hold
        n += 1
        while True:
            front = f1 // div
            if front < 10**9:
                break
            div *= 10
        
        s = time.time()
        first9 = sorted(list(str(f1//div)))
        m = time.time()
        last9 = sorted(list(str(f1%10**9)))
        e = time.time()
        if first9 == list('123456789') and last9 == list('123456789'):
            return n
        t1 += m-s
        t2 += e-m

start = time.time()
print(Euler104())
print(f'Took {time.time()-start}s')
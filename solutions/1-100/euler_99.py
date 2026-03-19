import itertools
import pathlib
import time
from math import *
from scripts.divisors import properDivisorsOf



def Euler99():
    raw = pathlib.Path('../resources/base_exp.txt').read_text()
    lines = raw.split('\n')
    maxLog = 0
    maxLine = 0
    for i in range(len(lines)):
        [base, exp] = lines[i].split(',')
        base, exp = int(base), int(exp)
        logResult = log(base) * exp
        if logResult > maxLog:
            maxLog = logResult
            maxLine = i
    return maxLine+1

start = time.time()
print(Euler99())
print(f'Took {time.time()-start}s')
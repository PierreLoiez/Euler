import time
from math import *
from scripts.divisors import distPrimeFact
from scripts.primes import primesUntilN
import tqdm

def sumOfFactOfDigs(n):
    return sum(factorial(int(d)) for d in str(n))

def Euler74():
    count = 0
    end = 10**6
    nonRepeatLengths = {}
    for n in range(1,end):
        
        sequence = [n]
        a = sumOfFactOfDigs(n)
        while a not in sequence and nonRepeatLengths.get(a, '')=='':
            sequence.append(a)
            a = sumOfFactOfDigs(a)
        baseLength = nonRepeatLengths.get(a, 0)
        sequence = sequence[::-1]
        for a in sequence:
            baseLength += 1
            nonRepeatLengths[a] = baseLength
        if baseLength == 60:
            count += 1
    return count

start = time.time()
print(Euler74())
print(f'Took {time.time()-start}s')
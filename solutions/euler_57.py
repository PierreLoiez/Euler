import time
from scripts.primes import *
from scripts.divisors import *
from math import *

def sumOfDigs(n):
    strN = str(n)

    return sum(int(d) for d in strN)
        
def Euler57():
    count = 0
    num, num_p = 3, 1
    den, den_p = 2, 1
    
    for _ in range(1000):
        num_p, num = num, 2*num + num_p
        den_p, den = den, 2*den+den_p
        if len(str(num))>len(str(den)):
            count += 1
    return count
    

start = time.time()
print(Euler57())
print(f'Took {time.time()-start}s')
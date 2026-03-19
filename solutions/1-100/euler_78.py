import time
from math import *
import numpy as np

def Euler78():
    partitions = [1]  
    n = 1
    divisor=1000000
    while True:
        p_n = 0
        k = 1
        
        # Using Euler's Pentagonal number theorem 
        while True:
            pent1 = k * (3*k - 1) // 2
            if pent1 > n:
                break
            
            pent2 = k * (3*k + 1) // 2
            sign = 1 if k % 2 == 1 else -1
            p_n += sign * partitions[n - pent1]
            if pent2 <= n:
                p_n += sign * partitions[n - pent2]
            
            k += 1
        
        p_n %= divisor
        partitions.append(p_n)
        
        if p_n == 0:
            return n
        
        n += 1
        

start = time.time()
print(Euler78())
print(f'Took {time.time()-start}s')
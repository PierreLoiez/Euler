import time
from math import *
import itertools

    

def getTripleFrom(s, t):
    return [s**2-t**2, 2*s*t, s**2+t**2]
    

def Euler94():
    primes = [[3,4,5]]
    total=0
    a,b,c = 3,4,5
    s=2
    t=1
    while c*3<=10**9:
        if gcd(a,b,c) == 1:
            # Can only be prime triangles since otherwise two sides are not coprime and so cannot form a diophantine equation around 1, needed for the 
            # almost-equalaterality of the triangle 
            if abs(a*2-c)==1: 
                print(a, b, c)
                total += 2*(a+c)
            if abs(b*2-c) == 1:
                print(a, b, c)
                total += 2*(b+c)
        t += 1
        if t==s:
            s+=1
            t=1
        [a,b,c] = getTripleFrom(s, t)
        
    return total

start = time.time()
print(Euler94())
print(f'Took {time.time()-start}s')
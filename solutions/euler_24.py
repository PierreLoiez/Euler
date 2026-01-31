from math import *
import time
def lexicoPerm(base, n):
    newOrder = ''
    for i in range(9, -1, -1):
            print(base)        
            newOrder += base[n//factorial(i)]
            base=base.replace(base[n//factorial(i)], '')
            n = n%factorial(i)
    return newOrder

def Euler24():
    base = '0123456789'
    n = 10**6-1
    
    return lexicoPerm(base, n)


start = time.time()
print(Euler24())
print(time.time()-start)
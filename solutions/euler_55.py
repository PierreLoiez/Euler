import time
from scripts.primes import *
from scripts.divisors import *
from math import *

def isPalindrome(n):
    return str(n) == str(n)[::-1]
def Euler55():
    count = 0
    for n in range(1, 10000):
        isLychrel = True
        l = n
        for _ in range(50):
            l += int(str(l)[::-1])
            if isPalindrome(l):
                isLychrel = False
                break
        if isLychrel:
            count += 1
    return count

start = time.time()
print(Euler55())
print(f'Took {time.time()-start}s')
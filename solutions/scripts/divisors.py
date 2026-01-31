from math import *

def divisorsOf(n):
    divs = []
    for i in range(1, int(sqrt(n))+1):
        if n%i == 0 and i != n//i:
            divs += [i, n//i]
        elif n%i == 0:
            divs.append(i)
    return divs

def properDivisorsOf(n):
    divs = []
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0 and i != n//i:
            divs += [i, n//i]
        elif n%i == 0:
            divs.append(i)
    return divs + [1]

def order(m, n): # returns Ord_m(n)
    l = 1
    if gcd(m, n)!=1 or m==1 or n == 1:
        return 0
    while n**l%m!=1:
        l+=1
    return l
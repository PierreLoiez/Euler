import time
from math import *
from scripts.divisors import properDivisorsOf
from numpy.polynomial import Polynomial




def Euler101():
    maxPower = 10
    truePoly = Polynomial([(-1)**i for i in range(maxPower+1)])
    print(truePoly)
    values = []
    for i in range(maxPower):
        roots = [truePoly(j) for j in range(1, i+2)]
        polys = []
        if len(roots) == 1:
            values.append(roots[0])
            continue
        for j in range(len(roots)):
            root1 = roots[j]
            basePol = Polynomial([1])
            for k in range(len(roots)):
                if j==k:
                    continue
                basePol = basePol * Polynomial(coef=[-(k+1), 1]) / (j-k)
            basePol = basePol * root1
            if basePol not in polys:
                polys.append(basePol)
        finalPol = sum(polys)
        n = 1
        while round(finalPol(n)) == round(truePoly(n)):
            n += 1
        values.append(round(finalPol(n)))
    return sum(values)


start = time.time()
print(Euler101())
print(f'Took {time.time()-start}s')
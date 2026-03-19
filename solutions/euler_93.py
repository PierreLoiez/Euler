import time
from math import *
import itertools

    
def resultOfEq(string):
    global result
    try:
        exec('global result\nresult='+string)
    except ZeroDivisionError:
        return 0
    return result

def getNthPerm(l, n):
    toRet = []
    copyL = l[:]
    for i in range(3, 0, -1):
        toRet.append(copyL.pop(n//factorial(i)))
        n%=factorial(i)
    toRet.append(copyL.pop())
    
    return toRet
    

def Euler93():
    best = 0
    bestN = ''
    operators = list('+-*/')
    for a in range(1, 10):
        for b in range(a+1, 10):
            for c in range(b+1, 10):
                for d in range(c+1, 10):
                    numbers = [str(e) for e in [a, b, c, d]]
                    results = []
                    for n1 in range(24):
                        a1,a2,a3,a4 = getNthPerm(numbers, n1)
                        for o1,o2,o3 in itertools.product(operators,operators,operators):
                            eqs = [
                                f'{a1}{o1}{a2}{o2}{a3}{o3}{a4}',
                                f'({a1}{o1}{a2}){o2}{a3}{o3}{a4}',
                                f'{a1}{o1}({a2}{o2}{a3}){o3}{a4}',
                                f'{a1}{o1}{a2}{o2}({a3}{o3}{a4})',
                                f'({a1}{o1}{a2}){o2}({a3}{o3}{a4})',
                                f'({a1}{o1}{a2}{o2}{a3}){o3}{a4}',
                                f'{a1}{o1}({a2}{o2}{a3}{o3}{a4})',
                                f'(({a1}{o1}{a2}){o2}{a3}){o3}{a4}',
                                f'{a1}{o1}(({a2}{o2}{a3}){o3}{a4})',
                                f'({a1}{o1}({a2}{o2}{a3})){o3}{a4}',
                                f'{a1}{o1}({a2}{o2}({a3}{o3}{a4}))',
                            ]
                            results.extend(resultOfEq(eq) for eq in eqs)
                    results.sort()
                    copyResult = results[:]
                    results = []
                    results.extend(int(r) for r in copyResult if r%1 == 0 and r > 0)
                    results = list(set(results))
                    for i in range(len(results)):
                        if results[i]!=i+1:
                            break
                    if i > best:
                        best = i
                        bestN = ''.join(numbers)
                        print(i, bestN)
    return bestN

start = time.time()
print(Euler93())
print(f'Took {time.time()-start}s')
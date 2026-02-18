import time
from scripts.primes import primesUntilLen, isPrime
import itertools



def Euler62():
    cubesWithDigs = {}
    found = False
    n = 1
    while not found:
        nc = n**3
        key = ''.join(sorted(list(str(nc))))
        listOfCubes = cubesWithDigs.get(key, [])
        listOfCubes.append(nc)
        cubesWithDigs[key] = listOfCubes
        if len(listOfCubes) == 5:
            return listOfCubes
        n += 1
        print(n)

start = time.time()
print(Euler62())
print(f'Took {time.time()-start}s')
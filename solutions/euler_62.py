import time
from scripts.primes import primesUntilLen, isPrime
import itertools



def Euler62():
    cubesWithDigs = {}
    found = False
    n = 1
    while not found:
        # Creates a repertoire of all the cubes sorted by their digits, and stops when one of the sections becomes bigger than 5
        nc = n**3 # done so n**3 doesn't need to be calculated multiple times
        key = ''.join(sorted(list(str(nc))))
        listOfCubes = cubesWithDigs.get(key, [])
        listOfCubes.append(nc)
        cubesWithDigs[key] = listOfCubes
        if len(listOfCubes) == 5:
            return listOfCubes[0]
        # Since the program appends bigger and bigger cubes, the first one in the list is the smallest
        n += 1
        print(n)

start = time.time()
print(Euler62())
print(f'Took {time.time()-start}s')
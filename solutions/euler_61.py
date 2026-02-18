import time
from scripts.primes import primesUntilLen, isPrime
import itertools



def Euler61():
    bools = [True, True, True, True, True, True]
    # A list of booleans that track whether we've exceeded 4 digits for each polygonal number
    allValues = {str(i): [[] for _ in range(6)] for i in range(10, 100)} | {
        f'0{str(i)}': [[] for _ in range(6)] for i in range(10)
    } # A dictionary of empty lists sorted by the numbers that could be at the beginning or the end of a polygonal number
    n = 5
    while any(bools):
        # Fills out the dictionary, putting each number in their section and the list corresponding to their type
        newVals = [n*(n+1)//2, n**2, n*(3*n-1)//2, n*(2*n-1), n*(5*n-3)//2, n*(3*n-2)]
        for i in range(6):
            val = str(newVals[i])
            bools[i] = len(val)<=4
            if len(val) == 4:
                allValues[val[:2]][i].append(val)
        n += 1
    for a, b, c, d, e in itertools.product(range(6), range(6), range(6), range(6), range(6)):
        if len({a, b, c, d, e}) == 5:
            # For each permutation of the numbers 0 to 6, check with sets
            f = 15-sum([a, b, c, d, e])
            for end, l1 in allValues.items():
                # Grabbing the right list for each condition : beginning of number i has to be the end of number i+1
                l1 = l1[a]
                for n1 in l1:

                    l2 = allValues[n1[2:]][b]
                    for n2 in l2:
                        l3 = allValues[n2[2:]][c]
                        for n3 in l3:
                            l4 = allValues[n3[2:]][d]
                            for n4 in l4:
                                l5 = allValues[n4[2:]][e]
                                for n5 in l5:
                                    l6 = allValues[n5[2:]][f]
                                    for n6 in l6:
                                        if n6[2:] == end:
                                            return int(n1) + int(n2) + int(n3) + int(n4) + int(n5) + int(n6)

start = time.time()
print(Euler61())
print(f'Took {time.time()-start}s')
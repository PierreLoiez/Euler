import time
from math import *
import itertools

    

def Euler90():
    needs = ['01', '04', '09', '16', '25', '36', '49', '64', '81']
    arrangements = 0
    checked = {}
    possibleCombos = []
    for a in range(10):
        for b in range(a+1, 10):
            for c in range(b+1, 10):
                for d in range(c+1, 10):
                    for e in range(d+1, 10):
                        possibleCombos.extend((a, b, c, d, e, f) for f in range(e+1, 10))

    for d1i in range(210):
        d1 = possibleCombos[d1i]
        for d2i in range(d1i+1, 210):
            d2 = possibleCombos[d2i]
            possibilities = []

            for x in d1:
                for y in d2:
                    if x in [6, 9]:
                        possibilities.extend(
                            (
                                str(6) + str(y),
                                str(9) + str(y),
                                str(y) + str(6),
                                str(y) + str(9),
                            )
                        )
                    elif y in [6, 9]:

                        possibilities.extend(
                            (
                                str(6) + str(x),
                                str(9) + str(x),
                                str(x) + str(6),
                                str(x) + str(9),
                            )
                        )
                    else:
                        possibilities.extend((str(x)+str(y), str(y)+str(x)))
            valid = all(sq in possibilities for sq in needs)
            if valid:
                arrangements += 1
    return arrangements
            

start = time.time()
print(Euler90())
print(f'Took {time.time()-start}s')
import time
import itertools

from math import *

def Euler33():
    pairs = []
    digs = '123456789'
    for common, a, b in itertools.product(digs, range(1, 10), range(1, 10)):
        if a<b:
            num1, den1 = int(common+str(a)), int(str(b)+common)
            if num1<den1 and num1/den1 == a/b:
                pairs.append((a, b))

            num2, den2 = int(str(a)+common), int(common+str(b)) # We only consider these two cases since the other cases are the trivial ones
            if num2<den2 and num2/den2 == a/b:
                pairs.append((a, b))
    numProd = 1
    denProd = 1
    for pair in pairs:
        numProd = numProd*pair[0]
        denProd = denProd*pair[1]
    return denProd / gcd(numProd, denProd)


start = time.time()
print(Euler33())
print(f'Took {time.time()-start}s')
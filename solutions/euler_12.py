from scripts.divisors import divisorsOf
import time

def Euler12():
    divs = []
    triangle = 1
    i = 2
    while len(divs) <500:
        triangle += i
        i += 1
        divs = divisorsOf(triangle)
    return triangle


start = time.time()
print(Euler12())
print(f'Took {time.time()-start}s')
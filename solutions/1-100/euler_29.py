import itertools
import time

def Euler29():
    numbers = {}
    for a, b in itertools.product(range(2, 101), range(2, 101)):
        n = a**b
        if numbers.get(n, 0) == 0:
            numbers[n] = 1
    return len(numbers.keys())

start = time.time()
print(Euler29())
print(f'Took {time.time()-start}s')
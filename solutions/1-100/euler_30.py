import itertools
import time

def Euler30():
    maxN = 9**5*len(str(9**5))
    total = 0
    for i in range(2**5, maxN):
        sumOf5thPowD = sum(int(j)**5 for j in str(i))
        if sumOf5thPowD == i:
            total += i
            print(i)
    return total

start = time.time()
print(Euler30())
print(f'Took {time.time()-start}s')
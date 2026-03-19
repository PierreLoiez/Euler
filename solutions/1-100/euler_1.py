
import time

def Euler1():
    return sum(i for i in range(1000) if i%3==0 or i%5 == 0)


start = time.time()
print(Euler1())
print(f'Took {time.time()-start}s')
import scripts.primes as primes
import time
def Euler7():
    return primes.primesUntilLen(10001)[-1]

start = time.time()
print(Euler7())
print(f'Took {time.time()-start}s')
import scripts.primes as primes
import time

def Euler10():
    prime_list = primes.primesUntilN(2*10**6)
    return sum(prime_list)
start = time.time()
print(Euler10())

print(f'Took {time.time()-start}s')
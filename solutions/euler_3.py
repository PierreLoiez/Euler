
from math import *
import scripts.primes as primes


def Euler3():
    primes_list = primes.primesUntilN(int(sqrt(600851475143)))
    return next(
        (prime for prime in primes_list[::-1] if 600851475143 % prime == 0),
        'Error: found no prime divisors',
    )

print(Euler3())
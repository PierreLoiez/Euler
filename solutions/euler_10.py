import scripts.primes as primes


def Euler10():
    prime_list = primes.primesUntilN(2*10**6)
    return sum(prime_list)

print(Euler10())
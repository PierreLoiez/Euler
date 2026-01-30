import scripts.primes as primes

def Euler7():
    return primes.primesUntilLen(10001)[-1]

print(Euler7())
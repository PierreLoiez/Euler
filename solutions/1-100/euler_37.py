import time
from scripts.primes import isPrime, primesUntilN




def Euler37():
    trunkPrimes = []
    maxVal = 10000
    primes = primesUntilN(maxVal)
    i = 4
    print(isPrime(7, primes), isPrime(3, primes))
    while len(trunkPrimes) < 11:
        p = primes[i]
        
        for l in range(1, len(str(p))):
            p1 = int(str(p)[:l])
            p2 = int(str(p)[l:])
            isPrime2 = False
            isPrime1 = isPrime(p1, primes)
            if not isPrime1:
                break
            
            isPrime2 = isPrime(p2, primes)
            if not isPrime2:
                break
        if isPrime2 and isPrime1:
            trunkPrimes.append(p)
            print(p)
        i += 1
        if i== len(primes):
            maxVal = 10 * maxVal
            primes = primesUntilN(maxVal)
    return sum(trunkPrimes)


start = time.time()
print(Euler37())
print(f'Took {time.time()-start}s')
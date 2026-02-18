import time
from scripts.primes import primesUntilLen, isPrime
from tqdm import tqdm

def checkNewPrimeInList(p, newPrime):
    n1 = int(str(p)+str(newPrime))
    n2 = int(str(newPrime)+str(p))
    if not isPrime(n1, primes):
        if p == 673 and newPrime == 109:
            print(n1, n2, "Fail")
        return False
    elif not isPrime(n2, primes):
        if p == 673 and newPrime == 109:
            print(n1, n2, "Fail")
        return False
    return True

def Euler60():
    n_primes=2000

    global primes
    primes = primesUntilLen(10000)
    smallerThatFit = {}
    for a in range(1, n_primes):
        smallerThatFit[primes[a]] = []
        for b in range(a):
            if checkNewPrimeInList(primes[b], primes[a]):
                smallerThatFit[primes[a]].append(primes[b])
    for p1, smaller1 in smallerThatFit.items():
        for p2 in smaller1:
            smaller2 = smallerThatFit[p2]
            for p3 in smaller2:
                if p3 not in smaller1:
                    continue
                smaller3 = smallerThatFit[p3]
                for p4 in smaller3:
                    if p4 not in smaller2:
                        continue
                    if p4 not in smaller1:
                        continue
                    smaller4 = smallerThatFit[p4]
                    for p5 in smaller4:
                        if p5 not in smaller3:
                            continue
                        if p5 not in smaller2:
                            continue
                        if p5 not in smaller1:
                            continue
                        return p1 + p2 + p3 + p4 + p5
    return None

start = time.time()
print(Euler60())
print(f'Took {time.time()-start}s')
import scripts.primes as primes

def Euler5():
    prime_list = primes.primesUntilN(20)
    result= 1
    for p in prime_list:
        n = 1
        while p**(n+1)<20:
            n+=1
        result = result * p**n
    return result  

print(Euler5())

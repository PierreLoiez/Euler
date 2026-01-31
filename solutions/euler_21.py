import scripts.divisors as divisors

def isAmicable(n):
    divsn = divisors.properDivisorsOf(n)
    d = sum(divsn)
    divsd = divisors.properDivisorsOf(d)
    sbn = sum(divsd)
    if sbn == n and n!=d:
        print(d, n)
    return sbn == n and n!=d

def Euler21():
    return sum(i for i in range(10000) if isAmicable(i))

print(Euler21())
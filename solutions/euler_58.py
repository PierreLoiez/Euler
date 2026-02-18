import time
from scripts.primes import isPrime, primesUntilN



def Euler58():
    total = 1
    total_p = 0
    primes = primesUntilN(100000)
    n = 1
    side = 0 # Stores the length of the side of the current square -1 (used to increment n)
    turn = 0 # Stores the way we are pointed in the square (0 is left, 1 is down, 2 is right and 3 is up)
    under10Pct = False
    while not under10Pct:
        if turn == 0:
            side += 2 # When we complete a full rotation, the square is 2 units bigger. This is when we check the ratio of primes
            under10Pct = total_p/total <= 0.1 and total_p != 0
        turn = (turn+1)%4
        n += side
        if isPrime(n, primes):
            total_p += 1
        total += 1
    return side-1 # Side is iterated once, and the tool is even while the actual length of the side is odd. So we have -2+1 i.e. -1

start = time.time()
print(Euler58())
print(f'Took {time.time()-start}s')
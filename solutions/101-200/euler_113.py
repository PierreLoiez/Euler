import time
from math import *
from scripts.primes import isPrime, primesUntilN
from itertools import permutations



def Euler113():
    repertoire = {(1, i):(1, 1) for i in range(1, 10)}
    # I tried brute forcing it (in a clever way) but for obvious reasons, that did not work. 
    # This approach is based on the fact that any increasing/decreasing number is composed of increasing/decreasing numbers resp. 
    # Keeping the number of increasing (decreasing) numbers of n digits whose first digit was i meant that to find the number of inc (dec) numbers 
    # of a digit longer would be the sum over the previous number of digits (plus one for decreasing since we have to account for 0) which are bigger (smaller)
    # than the current first digit. It is very, very fast  
    n_max = 100
    for n in range(2, n_max+1):
        for dig1 in range(1, 10):
            n_inc = sum(non_bouncy[0] for non_bouncy in [repertoire[(n-1, i)] for i in range(dig1, 10)])
            n_dec = sum(non_bouncy[1] for non_bouncy in [repertoire[(n-1, i)] for i in range(dig1, 0, -1)])+1
            repertoire[(n, dig1)] = (n_inc, n_dec)
    print(sum(v[0] for v in repertoire.values())+sum(v[1] for v in repertoire.values()) - 9*n_max)



start = time.time()
print(Euler113())
print(f'Took {time.time()-start}s')
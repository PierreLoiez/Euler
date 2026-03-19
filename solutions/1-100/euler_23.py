from scripts.divisors import properDivisorsOf
import time
def Euler23():
    abundant = []
    abundant.extend(i for i in range(1, 28123) if sum(properDivisorsOf(i))>i)
    allInts = {i:i for i in range(1, 28123)}
    for i in range(len(abundant)):
        
        for j in range(i, len(abundant)):
            ab1, ab2 = abundant[i], abundant[j]
            if ab1+ab2>28123:
                break
            allInts[ab1+ab2] = 0
        
    return sum(list(allInts.values()))
start = time.time()
print(Euler23())
print(f'Took {time.time()-start}s')
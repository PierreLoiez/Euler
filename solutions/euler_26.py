import time
import scripts.divisors as d

def Euler26():
    best = 0
    for i in range(2, 1000):
        m = i
        while m%2==0:
            m=m//2
        while m%5==0:
            m=m//5
        l = d.order(m, 10)
        if l>best:
            best = l
            besti=i
            print(best, besti)
    return best, besti
    
    
    
start = time.time()
print(Euler26())
print(f'Took {time.time()-start}s')
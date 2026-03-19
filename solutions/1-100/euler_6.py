import time

def Euler6():
    total = 0
    totalsq = 0
    for i in range(1, 101):
        total += i
        totalsq += i**2
    return totalsq - total**2

start = time.time()
print(Euler6())
print(f'Took {time.time()-start}s')
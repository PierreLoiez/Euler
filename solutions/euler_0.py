import time
def Euler0():    
    return  sum((2*i+1)**2 for i in range(278000//2))

start = time.time()
print(Euler0())

print(f'Took {time.time()-start}s')

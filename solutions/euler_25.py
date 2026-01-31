from scripts.sequences import fibbonacciTillNDigs
import time
def Euler25():
    fib = fibbonacciTillNDigs(1000)
    return len(fib)

start = time.time()
print(Euler25())
print(f'Took {time.time()-start}s')
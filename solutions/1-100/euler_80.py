import time
from math import *
from decimal import *

def Euler80():
    # The instructions in the problem were a little unclear : were the decimals after the point? 
    # Or do they include the whole part of the root? Took a little trial and error
    getcontext().prec = 200
    total = 0
    for n in range(2, 101):
        if sqrt(n)%1!=0:
            sqrtN = list(str(Decimal(n)**Decimal(0.5)).split('.')[1])
            subtotal = sum(int(i) for i in sqrtN[:99]) + int(sqrt(n))
            total += subtotal
            print(n, subtotal, len(sqrtN))
    return total

start = time.time()
print(Euler80())
print(f'Took {time.time()-start}s')
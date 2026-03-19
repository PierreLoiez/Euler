import time
from math import *
import numpy as np

def Euler79():
    with open('../resources/keylog.txt') as file:
        keylogs = file.read()
    keylogs = keylogs.split('\n')
    order = list(set(''.join(keylogs)))
    for kl in keylogs:
        if len(kl)!=3:
            print(kl)
            continue
        for i in range(2):
            k = kl[i]
            nk = kl[i+1]
            if order.index(k)>order.index(nk):
                order[order.index(k)], order[order.index(nk)] = nk, k
    return ''.join(order)
            

start = time.time()
print(Euler79())
print(f'Took {time.time()-start}s')
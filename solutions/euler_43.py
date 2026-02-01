import time
from math import *
import itertools



def Euler43():
    digs = '1234567890'
    total = 0
    toDiv = [2, 3, 5, 7, 11, 13, 17]
    for a in digs[:9]:
        print(a)
        digs0 = digs.replace(a, '')
        for b in digs0:
            digs1 = digs0.replace(b, '')
            for c in digs1:
                digs2 = digs1.replace(c, '')
                for d in digs2:
                    digs3 = digs2.replace(d, '')
                    for e in digs3:
                        digs4 = digs3.replace(e, '')
                        for f in digs4:
                            digs5 = digs4.replace(f, '')
                            for g in digs5:
                                digs6 = digs5.replace(g, '')
                                for h in digs6:
                                    digs7 = digs6.replace(h, '')
                                    for i in digs7:
                                        digs8 = digs7.replace(i, '')
                                        
                                        segments = [int(b+c+d), int(c+d+e), int(d+e+f), int(e+f+g), int(f+g+h), int(g+h+i), int(h+i+digs8)]
                                        pandig = a+b+c+d+e+f+g+h+i+digs8
                                        cont = True
                                        for j in range(7):
                                            if segments[j] % toDiv[j] != 0:
                                                cont = False
                                                break
                                        if not cont:
                                            break
                                        total += int(pandig)
    return total

start = time.time()
print(Euler43())
print(f'Took {time.time()-start}s')
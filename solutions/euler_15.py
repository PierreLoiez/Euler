import time
from math import *

def Euler15():
    return factorial(40)//(factorial(20)**2) 
# To get from the top left to the bottom right, 20 instances of down and 20 instances of right are needed. 
# As such, it means only the number of arrangements is what interests us, i.e binom(10, 20), which is what is calculated here. 


start = time.time()
print(Euler15())
print(f'Took {time.time()-start}s')
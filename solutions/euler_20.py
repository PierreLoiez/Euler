from math import *

def Euler20():
    fact100 = str(factorial(100))
    return sum(int(d) for d in fact100)
    
print(Euler20())
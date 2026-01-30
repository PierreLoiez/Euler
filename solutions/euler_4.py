
import time
def checkPal(number):
    strNum = str(number)
    return strNum == strNum[::-1]

def Euler4():
    best=0
    for i in range(999, 100, -1):
        for j in range(i, 100, -1):
            if checkPal(i*j) and i*j>best:
                best = i*j
            if i*i<best:
                return best
    return best

start = time.time()
print(Euler4())
print(f'Took {time.time()-start}s')
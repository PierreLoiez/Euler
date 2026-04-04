import time
def Euler8():
    with open('./resources/euler_8_num.txt') as file:
        fullInt = ''.join(file.readline()[:-1] for _ in range(20))
    best = 0
    for i in range(len(fullInt)-13):
        num = fullInt[i:i+13]
        res = 1
        for dig in num:
            res = res*int(dig)
        if res>best:
            best=res
    return best

start = time.time()
print(Euler8())
print(f'Took {time.time()-start}s')

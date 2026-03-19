import time



def Euler40():
    chaper = ''
    i = 1
    while len(chaper)< 1000000:
        chaper += str(i)
        i += 1
    prod = 1
    ofInterest = [0, 9, 99, 999, 9999, 99999, 999999]
    for i in ofInterest:
        prod = prod*int(chaper[i])
    return prod


start = time.time()
print(Euler40())
print(f'Took {time.time()-start}s')
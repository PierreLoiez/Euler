import itertools
import time

def totalMoney(coins):
    return coins[0]*200 + coins[1]*100 + coins[2]*50 + coins[3]*20 + coins[4]*10 + coins[5]*5 + coins[6]*2
def Euler31():
    coins = [0, 0, 0, 0, 0, 0, 0]
    total = 0
    while coins[0]<1:
        print(coins)
        total += 1
        coins[6] += 1
        index = 6
        while totalMoney(coins) > 200:
            coins[index] =0
            index -= 1
            coins[index] +=1
    return total
            
        
    

start = time.time()
print(Euler31())
print(f'Took {time.time()-start}s')
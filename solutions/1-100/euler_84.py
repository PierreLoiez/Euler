import random
import time
from math import *
import numpy as np

def nextSquare(start, roll):
    land = (start+roll)%40
    CCSq = [2, 17, 33]
    CHSq = [7, 22, 36]
    global communityCards, chanceCards, CC, CH
    if land in CCSq:
        card = communityCards[CC]
        CC=(CC+1)%16
        if card == 1:
            land = 0
        elif card == 2:
            land = 10
    elif land in CHSq:
        card = chanceCards[CC]
        CH=(CH+1)%16
        if card == 1:
            land = 0
        elif card == 2:
            land = 10
        elif card == 3:
            land = 11
        elif card == 4:
            land = 24
        elif card == 5:
            land = 39
        elif card == 6:
            land = 5
        elif card in {7, 8}:
            land = 5 if land == 36 else 25 if land == 22 else 15
        elif card == 9:
            land = 28 if land == 22 else 12
        elif card == 10:
            land -= 3
    elif land == 30:
        land = 10
    return land


def Euler84():
    square = 0
    counts = {i:0 for i in range(40)}
    double_count = 0
    global communityCards, chanceCards, CC, CH
    CC, CH = 0, 0
    communityCards, chanceCards = list(range(1, 17)), list(range(1, 17))
    random.shuffle(communityCards)
    random.shuffle(chanceCards)
    dieType = 4
    for _ in range(1000000):
        d1, d2 = random.randint(1, dieType), random.randint(1, dieType)
        if d1 == d2:
            double_count += 1
        else:
            double_count = 0
        if double_count == 3:
            square = 10
            double_count = 0
        else:
            square = nextSquare(square, d1+d2)
        counts[square] += 1
    best3 = [0, 0, 0]
    bestInds = [0, 0, 0]
    for i in range(40):
        current = counts[i]
        for j in range(3):
            if current>best3[j]:
                best3.insert(j, current)
                bestInds.insert(j, i)
                bestInds.pop()
                best3.pop()
                break
    print(counts)
    return bestInds
start = time.time()
print(Euler84())
print(f'Took {time.time()-start}s')
import time
from scripts.primes import *
from scripts.divisors import *
from math import *


def isFlush(hand):
    suit = hand[0][1]
    return all(h[1] == suit for h in hand)

def convertToTuple(hand):
    tToReturn = []
    
    for card in hand:
        t = (strengths[card[0]], card[1])
        tToReturn.append(t)
    tToReturn.sort()
    return tToReturn

def isStraight(hand):
    strongest = hand[4][0]
    for i in range(4, -1, -1):
        strength = hand[i][0]
        if strongest-strength != 4-i:
            return False
    return strongest
    
def ofAKind(hand):
    best = 0
    bestStr = 0
    for i in range(len(hand)-1):
        card = hand[i]
        count = 1
        for j in range(i+1, len(hand)):
            otherCard = hand[j]
            if otherCard[0] == card[0]:
                count +=1
        if count >= best:
            best = count
            bestStr = card[0]
    return best, bestStr

def isFullHouse(hand):
    cardsStrengths = [card[0] for card in hand]
    greater = 0
    for s in cardsStrengths:
        if cardsStrengths.count(s) != 3 or cardsStrengths.count(s)!=2:
            return False
        if cardsStrengths.count(s) == 3:
            greater = s
    return greater

def isTwoPair(hand):
    strength = [card[0] for card in hand]
    for s in strength:
        if strength.count(s) not in [1, 2]:
            return False
        if strength.count(s) == 1:
            strength.remove(s)
    if len(strength) != 4:
        return False
    else:
        return strength[0], strength[3]

def Euler54():
    global strengths
    strengths = {str(i):i for i in range(2, 10)}
    strengths['T'], strengths['J'], strengths['Q'], strengths['K'], strengths['A'] = 10, 11, 12, 13, 14
    count = 0
    with open('../resources/poker.txt') as file:
        hands = file.read().split('\n')
    hands.remove('')
    p1hands = []
    p2hands = []
    for hand in hands:
        hand = hand.split(' ')
        p1hands.append(convertToTuple(hand[:5]))
        p2hands.append(convertToTuple(hand[5:]))
    for i in range(len(hands)):
        cb4 = count
        p1hand = p1hands[i]
        p2hand = p2hands[i]
        straights = [isStraight(p1hand), isStraight(p2hand)]
        flushes = [isFlush(p1hand), isFlush(p2hand)]
        fullHs = [isFullHouse(p1hand), isFullHouse(p2hand)]
        bestMultiples = [ofAKind(p1hand), ofAKind(p2hand)]
        have2pairs = [isTwoPair(p1hand), isTwoPair(p2hand)]
        if (straights[0] and flushes[0]) or (straights[1] and flushes[1]):
            if all([straights, flushes]):
                print(p1hand, p2hand)
            elif straights[0] and flushes[0]:
                count += 1
        elif bestMultiples[0][0] == 4 or bestMultiples[1][0] == 4:
            if bestMultiples[1][0] == 4 and bestMultiples[0][1] > bestMultiples[1][1]:
                count += 1
            elif bestMultiples[1][0] < 4:
                count += 1
        elif any(fullHs):
            if all(fullHs) and fullHs[0]>fullHs[1]:
                count += 1
            elif fullHs[0] and not all(fullHs):
                count += 1
        elif any(flushes):
            if flushes[0]:
                if flushes[1] and p1hand[4]> p2hand[4]:
                    count += 1
                elif not all(flushes):
                    count += 1
        elif any(straights):
            if straights[0]:
                if straights[1] or not straights[1] and not all(straights):
                    count += 1
        elif bestMultiples[0][0] == 3 or bestMultiples[1][0] == 3:
            if bestMultiples[0][0] == 3 and bestMultiples[1][0] == 3:
                if bestMultiples[0][1] > bestMultiples[1][1]:
                    count += 1
            elif bestMultiples[0][0] == 3:
                count += 1
        elif have2pairs[0] or have2pairs[1]:
            if have2pairs[0] and have2pairs[1]:
                if have2pairs[0][1]>have2pairs[1][1]:
                    count += 1
                elif have2pairs[0][1] == have2pairs[1][1] and have2pairs[0][0]>have2pairs[1][0]:
                    count += 1
            elif have2pairs[0]:
                count += 1
        elif bestMultiples[0][0] == 2 or bestMultiples[1][0] == 2:
            if bestMultiples[0][0] == 2 and bestMultiples[1][0] == 2:
                if bestMultiples[0][1] > bestMultiples[1][1]:
                    count += 1
                elif bestMultiples[0][1] == bestMultiples[1][1]:
                    i = 4
                    while p1hand[i]==p2hand[i]:
                        i -=1
                    count += 1 if p1hand[i]>p2hand[i] else 0
            elif bestMultiples[0][0] == 2:
                count += 1
        else:
            for i in range(4, -1, -1):
                if p1hand[i] == p2hand[i]:
                    show = True
                    continue
                elif p1hand[i] > p2hand[i]:
                    count += 1
                    break
                else:
                    break
            
    return count
    

start = time.time()
print(Euler54())
print(f'Took {time.time()-start}s')
import time
from math import *
from fractions import Fraction
from itertools import combinations


def Euler121():
    n_turns = 15
    balls = {turn:(1, turn+1) for turn in range(n_turns)}
    prob = Fraction(0, 1)
    for n_blue in range((n_turns+1)//2):
        bluePerms = list(combinations(balls.values(), n_blue))
        for blues in bluePerms:
            p = Fraction(1, 1)
            for turn in balls.values():
                if turn not in blues:
                    p *= Fraction(turn[0], sum(turn))
                else:
                    toMult = Fraction(turn[1], sum(turn))
                    p *= toMult
            prob += p
    return prob.denominator//prob.numerator
    


start = time.time()
print(Euler121())
print(f'Took {time.time()-start}s')
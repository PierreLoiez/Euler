import time
from math import *

def scoreWord(word):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    score = 0
    for c in word:
        score += characters.index(c)+1
    return score

def Euler42():
    triangles = [int(0.5*i*(i+1)) for i in range(100)]
    with open('./resources/words.txt') as file:
        words = file.readline().replace('"', '').split(',')
    return sum(scoreWord(word) in triangles for word in words)


start = time.time()
print(Euler42())
print(f'Took {time.time()-start}s')
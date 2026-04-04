import itertools
import pathlib
import time
from math import *
from scripts.divisors import properDivisorsOf

def permuteLike(toPerm, base, to):
    if len(set(toPerm)) != len(set(base)):
        return None
    permuted = ['0' for _ in toPerm]
    for i in range(len(toPerm)):
        char = toPerm[i]
        destination = to.index(base[i])
        permuted[destination] = char
    return ''.join(permuted)

def Euler98():
    raw = pathlib.Path('./resources/words2.txt').read_text()
    raw = raw.strip('"')
    words = raw.split('","')
    wordAnagrams = {}
    for word in words:
        key = tuple(sorted(word))
        wordAnagrams[key] = wordAnagrams.get(key, []) + [word]
    biggestLen = 0
    toRemove = []
    for key, anagrams in wordAnagrams.items():
        if len(anagrams)>1 and len(anagrams[0])>biggestLen:
            biggestLen=len(anagrams[0])
        elif len(anagrams)<2:
            toRemove.append(key)
    [wordAnagrams.__delitem__(key) for key in toRemove]
    squares = [j**2 for j in range(10**(biggestLen//2+1))]
    squareAnagrams = {}
    for square in squares:
        key = tuple(sorted(str(square)))
        squareAnagrams[key] = squareAnagrams.get(key, []) + [str(square)]
    toRemove = []
    toRemove.extend(
        key for key, anagrams in squareAnagrams.items() if len(anagrams) < 2
    )
    [squareAnagrams.__delitem__(key) for key in toRemove]
    maximum = 0
    for sqKey, wordKey in itertools.product(squareAnagrams.keys(), wordAnagrams.keys()):
        if len(sqKey) == len(wordKey):
            squares = squareAnagrams[sqKey]
            words = wordAnagrams[wordKey]
            for word1, word2 in itertools.product(words, words):
                if word1 == word2:
                    continue
                for square in squares:
                    permutedSq = permuteLike(square, list(word1), list(word2))
                    if permutedSq in squares and int(permutedSq)>maximum:
                        maximum = int(permutedSq)
    return maximum

start = time.time()
print(Euler98())
print(f'Took {time.time()-start}s')
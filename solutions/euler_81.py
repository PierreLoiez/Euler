import time
from math import *
import numpy as np

def PathFinder(matrix):
    costOfPosition = {(0,0):matrix[0,0]}
    openQueue = [(0,0)]
    while openQueue!=[]:
        s = openQueue.pop(0)
        for i in range(2):
            if s[i] >= 79:
                continue
            newS = (s[0] + (i+1)%2, s[1] + i%2)
            costNewS = costOfPosition[s] + matrix[newS]
            if costNewS>= costOfPosition.get(newS, 10**10):
                continue
            openQueue.append(newS)
            costOfPosition[newS] = costNewS
    
    return costOfPosition[(79,79)]


def Euler81():
    with open('./resources/matrix.txt') as file:
        matrix = file.read()
    matrix = matrix.split('\n')
    newMatrix = []
    newMatrix.extend([[int(i) for i in line.split(',')] for line in matrix])
    
    matrix = np.array(newMatrix)
    return PathFinder(matrix)

start = time.time()
print(Euler81())
print(f'Took {time.time()-start}s')
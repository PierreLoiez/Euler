import pathlib
import time
from math import *
import numpy as np

def PathFinder(matrix, pathMatrix = None):
    if pathMatrix is None:
        costOfPosition = {(0,0):[matrix[(0, 0)], []]}
    else:
        costOfPosition = pathMatrix
    openQueue = [(0,0)]
    smallest = 10**10
    while openQueue!=[]:
        s = openQueue.pop(0)
        for i in range(3):
            if s[1] == 79:
                continue
            if s[0] + (i%3-1)<0 or s[0] + (i%3-1)>79:
                continue
            newS = (s[0] + (i%3-1), s[1] + (i%3)%2)
            costNewS = matrix[newS] if newS[1] == 0 else costOfPosition[s][0] + matrix[newS]
            if costNewS>= costOfPosition.get(newS, [10**10, []])[0]:
                continue
            openQueue.append(newS)
            costOfPosition[newS] = [costNewS, []] if newS[1] == 0 else [costNewS, costOfPosition[s][1]+[s]]
    return costOfPosition


def Euler82():
    matrix = pathlib.Path('../resources/matrix.txt').read_text()
    matrix = matrix.split('\n')
    newMatrix = [[int(i) for i in line.split(',')] for line in matrix]
    matrix = np.array(newMatrix)
    costMatrix = PathFinder(matrix[:])
    endValues = []
    endValues.extend(costMatrix[(i, 79)][0] for i in range(80))
    return min(endValues)

start = time.time()
print(Euler82())
print(f'Took {time.time()-start}s')
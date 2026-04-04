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
    while openQueue!=[]:
        s = openQueue.pop(0)
        for i in range(4):
            if s[0] + (-1)**(i//2)*(i%2)<0 or s[0] + (-1)**(i//2)*(i%2)>79 or s[1] + (-1)**(i//2)*((i+1)%2)<0 or s[1] + (-1)**(i//2)*((i+1)%2)>79:
                continue
            newS = (s[0] + (-1)**(i//2)*(i%2), s[1] + (-1)**(i//2)*((i+1)%2))
            costNewS = costOfPosition[s][0] + matrix[newS]
            if costNewS>= costOfPosition.get(newS, [10**10, []])[0]:
                continue
            openQueue.append(newS)
            costOfPosition[newS] = [costNewS, []] if newS[1] == 0 else [costNewS, costOfPosition[s][1]+[s]]
    return costOfPosition


def Euler83():
    matrix = pathlib.Path('./resources/matrix.txt').read_text()
    matrix = matrix.split('\n')
    newMatrix = [[int(i) for i in line.split(',')] for line in matrix]
    matrix = np.array(newMatrix)
    costMatrix = PathFinder(matrix[:])
    return costMatrix[(79, 79)]

start = time.time()
print(Euler83())
print(f'Took {time.time()-start}s')
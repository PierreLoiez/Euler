import itertools
import numpy as np
import time
def Euler11():
    grid = []
    with open('./resources/euler_11.txt') as file:
        grid.extend(file.readline().split(" ") for _ in range(20))
    best = 0
    npGrid = np.asarray(grid)
    npGrid = npGrid.astype(np.int64)
    bestProd = []
    bestStart = (0, 0)
    for i, j in itertools.product(range(20), range(20)):
        if i < 16:
            res = np.prod(npGrid[i:i+4,j])
            if res>best:
                best = res
                bestProd = npGrid[i:i+4,j]
                bestStart = (i ,j)
        if j < 16:
            res = np.prod(npGrid[i,j:j+4])
            if res>best:
                best = res
                bestProd = npGrid[i,j:j+4]
                bestStart = (i ,j)
        if j<16 and i<16:
            res = np.prod([npGrid[i+k, j+k] for k in range(4)])
            if res>best:
                best = res
                bestProd = [npGrid[i+k, j+k] for k in range(4)]
                bestStart = (i ,j)
        if i<16 and j>3:
            res = np.prod([npGrid[i+k, j-k] for k in range(4)])
            if res>best:
                best = res
                bestProd = [npGrid[i+k, j+k] for k in range(4)]
                bestStart = (i ,j)
    return best, bestProd, bestStart
                
    
start = time.time()
print(Euler11())
print(f'Took {time.time()-start}s')
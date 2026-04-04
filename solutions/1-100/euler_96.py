import itertools
import time
from math import *
from scripts.divisors import properDivisorsOf

    
def isSolved(grid):
    for line in grid:
        for item in line:
            if type(item) == list:
                return False
    return True


def restrainPossibilities(grid):
    for l in range(9):
        for c in range(9):
            if type(grid[l][c]) == list:
                column = [grid[i][c] for i in range(9)]
                square = [grid[l-l%3+i%3][c-c%3+i//3] for i in range(9)]
                squarePs, columnPs, linePs = [s for s in square if type(s)==list], [s for s in column if type(s)==list], [s for s in grid[l] if type(s)==list]
                ofInt = grid[l][c]
                removes = []
                removes.extend(
                    possibility
                    for possibility in ofInt
                    if possibility in grid[l]
                    or possibility in column
                    or possibility in square
                )
                [grid[l][c].remove(p) for p in removes]
                if column.count(ofInt) == len(ofInt):
                    for a1 in ofInt:
                        for a2 in column:
                            if a1 in a2 and a2 != grid[l][c]:
                                a2.remove(a1)
                if grid[l].count(ofInt) == len(ofInt):
                    for a1 in ofInt:
                        for a2 in grid[l]:
                            if a1 in a2 and a2 != grid[l][c]:
                                a2.remove(a1)
                if square.count(ofInt) == len(ofInt):
                    for a1 in ofInt:
                        for a2 in square:
                            if a1 in a2 and a2 != grid[l][c]:
                                a2.remove(a1)
                breakAgain = False
                for p in ofInt:
                    sqCount = sum(i.count(p) for i in squarePs)
                    if sqCount == 1:
                        breakAgain = True
                        grid[l][c] = p
                        break
                    lineCount = sum(i.count(p) for i in linePs)
                    if lineCount == 1:
                        breakAgain = True
                        grid[l][c] = p
                        break
                    columnCount = sum(i.count(p) for i in columnPs)
                    if columnCount == 1:
                        breakAgain = True
                        grid[l][c] = p
                        break
                if breakAgain:
                    break
                if len(grid[l][c]) == 1:
                    grid[l][c] = grid[l][c][0]
    return grid

def copyGrid(grid):
    copy = [['0' for _ in range(9)] for _ in range(9)]
    for l, c in itertools.product(range(9), range(9)):
        copy[l][c] = grid[l][c][:] if type(grid[l][c]) == list else grid[l][c]
    return copy

def isBroken(grid):
    for line in grid:
        for item in line:
            if item == []:
                return True
    return False

def displayGrid(grid):
    for line in grid:
        print(line)
    print()

def Solve(grid):
    newGrid, oldGrid = copyGrid(grid), copyGrid(grid)
    while not isSolved(newGrid):
        oldGrid = copyGrid(newGrid)
        newGrid = restrainPossibilities(newGrid)
        if newGrid == oldGrid:
            for l, c in itertools.product(range(9), range(9)):
                if type(newGrid[l][c])==list:
                    for opt in newGrid[l][c]:
                        trial = copyGrid(newGrid)
                        trial[l][c] = opt
                        trial = Solve(trial)
                        if trial != None:
                            return trial
                        else:
                            continue
                    if trial is None:
                        return None
        if isBroken(newGrid):
            return None
    return newGrid

def Euler96():
    with open('./resources/sudoku.txt') as file:
        rawString = file.read()[1:]
    raw = rawString.split('Grid ')
    sudokus = []
    sudokus.extend(s.split('\n')[1:10] for s in raw)
    total = 0
    for sudo in sudokus:
        sudoku = []
        print(sudokus.index(sudo))
        sudoku.extend(list(s) for s in sudo)
        for line, i in itertools.product(sudoku, range(9)):
            if line[i] == '0':
                line[i] = list('123456789')
        solvedS = Solve(sudoku)
        print('Solved! ' if isSolved(solvedS) else 'Oh dear...')
        displayGrid(solvedS)
        total += int(''.join(solvedS[0][:3]))
    return total

start = time.time()
print(Euler96())
print(f'Took {time.time()-start}s')
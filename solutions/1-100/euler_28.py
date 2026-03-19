import time
import numpy as np



def Euler28():
    total = 0
    side_final = 1001
    n = 1
    side = 0 # Stores the length of the side of the current square -1 (used to increment n)
    turn = 0 # Stores the way we are pointed in the square (0 is left, 1 is down, 2 is right and 3 is up)
    while n<=side_final**2:
        total += n
        if turn == 0:
            side += 2 # When we complete a full rotation, the square is 2 units bigger
        turn = (turn+1)%4
        n += side
    return total

start = time.time()
print(Euler28())
print(f'Took {time.time()-start}s')
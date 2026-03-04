import time
from math import *
import itertools



def Euler68():
    needs = '1234567890'
    seen = {}
    biggest=0
    for n in range(factorial(10)):
        arrangement = []
        digs = list(needs)
        n1 = n
        # Create a permutation of all 10 digits and replace 0 with 10
        for i in range(10, 0, -1):
            arrangement.append(digs.pop(n1%i))
            if arrangement[-1] == '0':
                arrangement[-1] = '10'
            n1 = n1 // i
        # Ignore the arrangement that would make a 17 digit string
        if arrangement[1] == '10' or arrangement[2] == '10' or arrangement[4] == '10' or arrangement[6] == '10' or arrangement[8] == '10':
            continue
        # Create the magic gon ring
        numbersUnprocessed = [[int(arrangement[0]), int(arrangement[1]), int(arrangement[2])], 
                   [int(arrangement[3]), int(arrangement[2]), int(arrangement[4])], 
                   [int(arrangement[5]), int(arrangement[4]), int(arrangement[6])], 
                   [int(arrangement[7]), int(arrangement[6]), int(arrangement[8])], 
                   [int(arrangement[9]), int(arrangement[8]), int(arrangement[1])]]
        sortedNums = sorted(numbersUnprocessed)
        numbers = []
        # Arrange the ring in the way the problem explains
        numbers.extend(
            numbersUnprocessed[i % 5]
            for i in range(
                numbersUnprocessed.index(sortedNums[0]),
                5 + numbersUnprocessed.index(sortedNums[0]),
            )
        )
        # Ignore copies
        if seen.get(str(numbers), False):
            continue
        seen[str(numbers)] = True
        number = int(''.join(str(numbers[j][k]) for j in range(5) for k in range(3)))
        if (
            all(sum(numbers[j]) == sum(numbers[0]) for j in range(5))
            and number > biggest
        ):
            biggest = number
    return biggest
start = time.time()
print(Euler68())
print(f'Took {time.time()-start}s')
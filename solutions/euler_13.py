import time

def Euler13():
    numbers = []
    with open('resources/euler_13_nums.txt') as file:
        numbers.extend(int(file.readline()) for _ in range(100))
    total = str(sum(numbers))
    return total[:10]
    
start = time.time()
print(Euler13())
print(f'Took {time.time()-start}s')
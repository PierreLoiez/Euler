import time
def Euler22():
    with open('./resources/names.txt') as file:
        names = file.readline().replace('"', '').split(',')
    names.sort()
    allChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    scores = {allChars[i]:i+1 for i in range(len(allChars))}
    return sum(
        sum(scores[char] for char in names[i]) * (i + 1)
        for i in range(len(names))
    )

start = time.time()
print(Euler22())
print(f'Took {time.time()-start}s')
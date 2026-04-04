

def Euler18():
    pyramid = []
    with open('./resources/euler_18.txt') as file:
        pyramid.extend(line.split(' ') for line in file)
    for i in range(len(pyramid)):
        pyramid[i] = list(map(int, pyramid[i]))
    for i in range(len(pyramid)-1, 0, -1):
        bottomRow = pyramid[i]
        topRow = pyramid[i-1]
        print(bottomRow)
        for j in range(len(topRow)):
            topRow[j] += max(bottomRow[j], bottomRow[j+1])
    return pyramid[0][0]

print(Euler18())
import json

def Euler17():
    with open('./resources/nums_as_words.json') as file:
        numAsName = json.load(file)
    total = 0
    for i in range(1, 1001):
        strI = str(i)
        if len(strI)==3:
            if strI[1] == strI[2] == '0':
                name = f'{numAsName[strI[0]]}hundred{numAsName[str((i%100) // 10 * 10)]}{numAsName[str(i % 10)]}'
            elif str(i%100) in numAsName.keys():
                name = f'{numAsName[strI[0]]}hundredand{numAsName[str(i%100)]}'
            else:
                name = f'{numAsName[strI[0]]}hundredand{numAsName[str((i%100) // 10 * 10)]}{numAsName[str(i % 10)]}'

        elif len(strI) ==4:
            name = 'onethousand'
        elif len(strI) == 2:
            if str(i) in numAsName.keys():
                name = numAsName[str(i)]
            else:
                name = f'{numAsName[str(i//10*10)]}{numAsName[str(i%10)]}'
        else:
            name = numAsName[str(i)]
        total += len(name)
    return total

print(Euler17())
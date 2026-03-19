
def Euler16():
    twoTo1000 = str(2**1000)
    total = 0
    for dig in twoTo1000:
        total += int(dig)
    return total

print(Euler16())
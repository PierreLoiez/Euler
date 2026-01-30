

def Euler9():
    for a in range(1, 1000):
        for b in range(a, 1000):
            c = 1000-a-b
            if c<0:
                break
            if a**2+b**2 == c**2:
                return a*b*c
            
print(Euler9())
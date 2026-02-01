import time
import itertools

def hasDigs(n, digs):
    if len(str(n)) != len(digs):
        return False
    for d in str(n):
        if d not in digs:
            return False
    return all(d in str(n) for d in digs)

def Euler32():
    digits = '123456789'
    products = {}
    for a in digits:
        digits0 = digits.replace(a, '')
        for b in digits0:
            digits1 = digits0.replace(b, '')
            for c in digits1:
                digits2 = digits1.replace(c, '')
                for d in digits2:
                    digits3 = digits2.replace(d, '')
                    for e in digits3:
                        digits4 = digits3.replace(e, '') # Composing products with not repeating digits
                        p1, p2 = int(a+b+c), int(d+e)
                        prod = p1*p2
                        if hasDigs(prod, digits4):
                            products[prod] = 1
                        
                        
                        p1, p2 = int(a+b+c+d), int(e)
                        prod = p1*p2
                        if hasDigs(prod, digits4):
                            products[prod] = 1
    return sum(products.keys())
        


start = time.time()
print(Euler32())
print(f'Took {time.time()-start}s')
import pathlib
import time
import itertools


def toBinary(n):
    toReturn = []
    while len(toReturn)<8:
        toReturn += str(n%2)
        n = n//2
    return toReturn[::-1]

def toBase10(binary):
    binary = binary[::-1]
    return sum(int(binary[i])*2**i for i in range(8))

def toAscii(string):
    toRet = []
    for c in string:
        toRet += toBinary(ord(c))
    return toRet

def decode(msg, key):
    
    return ''.join(chr(msg[i]^ord(key[i%len(key)])) for i in range(len(msg)))

def Euler59():
    raw_msg = pathlib.Path('./resources/cipher.txt').read_text()
    raw_msg = raw_msg.split(',')
    raw_msg = [int(c) for c in raw_msg]
    possibleChars = [chr(i) for i in range(ord('a'), ord('z')+1)]

    for cs in itertools.product(possibleChars, possibleChars, possibleChars):
        key = ''.join(cs)
        decoded = decode(raw_msg, key)
        decodedL = list(decoded)
        if ' and ' in decoded:
            print(decoded)
            break
    return sum(ord(c) for c in decoded)
start = time.time()
print(Euler59())
print(f'Took {time.time()-start}s')
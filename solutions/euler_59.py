import pathlib
import time
import itertools

def decode(msg, key):
    # Using in-build XOR operation in python
    return ''.join(chr(msg[i]^ord(key[i%len(key)])) for i in range(len(msg)))

def Euler59():
    raw_msg = pathlib.Path('./resources/cipher.txt').read_text()
    raw_msg = raw_msg.split(',')
    raw_msg = [int(c) for c in raw_msg]
    possibleChars = [chr(i) for i in range(ord('a'), ord('z')+1)]

    for cs in itertools.product(possibleChars, possibleChars, possibleChars):
        key = ''.join(cs)
        decoded = decode(raw_msg, key)
        if ' and ' in decoded:
            print(decoded)
            break
    return sum(ord(c) for c in decoded)
start = time.time()
print(Euler59())
print(f'Took {time.time()-start}s')
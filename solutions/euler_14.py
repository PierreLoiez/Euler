import time
def Collatz(n_0, done):
    n=n_0
    sequence = []
    while n != 1:
        sequence.append(n)
        if done.get(n, 0) != 0:
            done[n_0] = sequence + done[n]
            return sequence + done[n], done
        n = n/2 if n%2 == 0 else n*3+1
    done[n_0] = sequence
    return sequence, done

def Euler14():
    done = {}
    bestSeq = []
    bestN = 0
    for i in range(2, 1*10**6):
        seq, done = Collatz(i, done)
        if len(seq)> len(bestSeq):
            bestSeq = seq
            bestN = i
    return bestN
start = time.time()
print(Euler14())
print(f'Took {time.time()-start}s')
import time
from math import *
from scripts.primes import isPrime, primesUntilN




def Euler109():
    options = ['S', 'D', 'T'] # The possible sections on the board
    scores = {i:set() for i in range(1, 61)}
    for i in range(1, 21): # We iterate through the segments 1 - 20
        for opt in options:
            mod = 1 if opt == 'S' else 2 if opt == 'D' else 3 # We add the part of the board to the corresponding score
            scores[i*mod].add(opt+str(i))
    scores[25].add('S25') # Place bullseye separately
    scores[50].add('D25')
    for i in range(1, 61): # Remove empty lists from the dictionary
        if scores[i] == []:
            scores.__delattr__(i)
    number_options = 0
    for score in range(2, 100): #The range of scores we wish to find arrangements for
        third = 50 
        # Bullseye is a bit strange so we do it separately. 
        # The idea is to define the final (and necessarily double) throw first and find arrangements around that
        if score-third == 0: # If the score is completed by the double throw alone, that is one arrangement
            number_options += 1
        else:
            for second in scores.keys(): # We scour the possible values for a second throw
                if score-second-third <0: # If we overshoot, we break the loop (the throws are in increasing value)
                    break
                elif score-second-third == 0:
                    # If the values of the first and second throws complete the score, that is one arrangement per throw that corresponds to the "second" score
                    
                    number_options += len(scores[second])
                    break
                elif second <= score-second-third: 
                    # If we still need a throw, we check that the value needed can be achieved, and to avoid symmetry we impose that 
                    # the "final throw" (non double) has to be greater than the second throw. 
                    try:
                        number_options += len(scores[second]) * len(scores[score-second-third]) if scores[second]!=scores[score-second-third] else len(scores[second]) * (len(scores[score-second-third])+1)//2
                        # There are 2 possibilities: 
                        # 1: Both scores are distinct, in which case there is no overlap and the number of combinations is the product of the lengths of the possible arrangements. 
                        # 2: Both scores are identical, in which case the number of combinations is the sum between the length of the list and 1
                    except KeyError:
                        pass
        for third in range(2, min(score, 40)+1, 2): #We then do the same but for every double score (i.e. double 1 through double 20)
            if score-third == 0:
                number_options += 1
            else:
                for second in scores.keys():
                    if score-second-third <0:
                        break
                    elif score-second-third == 0:
                        number_options += len(scores[second])
                        break
                    elif second <= score-second-third:
                        try:
                            number_options += len(scores[second]) * len(scores[score-second-third]) if scores[second]!=scores[score-second-third] else len(scores[second]) * (len(scores[score-second-third])+1)//2
                        except KeyError:
                            pass
                            
    return number_options


start = time.time()
print(Euler109())
print(f'Took {time.time()-start}s')
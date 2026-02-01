import time
from matplotlib.image import imread, imsave
import numpy as np


def Euler():
    img = imread('./resources/bonus_secret_statement.png')
    
    img = np.mean(img, axis=2)
    h = np.shape(img)[0]
    w = np.shape(img)[1]
    img = img.flatten()
    matrix = []
    for i in range(len(img)):
        print(i)
        line = [0 for _ in img]
        ogCoords = (i%h, i//h)
        newCoords = [((ogCoords[0]+1)%h, ogCoords[1]), ((ogCoords[0]-1)%h, ogCoords[1]), (ogCoords[0], (ogCoords[1]+1)%w), (ogCoords[0], (ogCoords[1]-1)%w)]
        coordsToI = [c[0] + c[1]*h for c in newCoords]
        for j in coordsToI:
            line[j] = 1
        matrix.append(line)
    imsave('test.png', matrix)
    
    
print(Euler())

import contextlib
import pathlib
import time
from math import *
from scripts.divisors import properDivisorsOf
from numpy.polynomial import Polynomial


def triangleContains0(A, B, C):
    if (A[0]<0 and B[0]<0 and C[0] <0) or (A[1]<0 and B[1]<0 and C[1] <0) or (A[0]>0 and B[0]>0 and C[0] >0) or (A[1]>0 and B[1]>0 and C[1] >0):
        return False
    if A[0]*B[0]<=0:
        line1at0 = -(B[1] - A[1])/(B[0]-A[0])*A[0] + A[1]
    else:
        line1at0 = None
    if C[0]*B[0]<=0:
        line2at0 = -(B[1] - C[1])/(B[0]-C[0])*C[0] + C[1]
    else:
        line2at0 = None
    if A[0]*C[0]<=0:
        line3at0 = -(C[1] - A[1])/(C[0]-A[0])*A[0] + A[1]
    else:
        line3at0 = None
    if line1at0 is None:
        if line2at0 is None or line3at0 is None:
            return False
        return line2at0*line3at0<=0
    elif line2at0 is None:
        return False if line3at0 is None else line1at0*line3at0<=0
    elif line3at0 is None:
        return line1at0*line2at0 <=0
    if line1at0*line2at0 <=0 or line2at0*line3at0<=0 or line1at0*line3at0<=0:
        return True



def Euler102():
    raw = pathlib.Path('./resources/triangles.txt').read_text()
    triangles = raw.split('\n')
    triangles.remove('')
    total = 0
    print(triangleContains0([-340,495], [-153,-910], [835,-947]))
    for t in triangles:
        points = t.split(',')
        A = [int(points[0]), int(points[1])]
        B = [int(points[2]), int(points[3])]
        C = [int(points[4]), int(points[5])]
        if triangleContains0(A, B, C):
            total += 1
    return total

start = time.time()
print(Euler102())
print(f'Took {time.time()-start}s')
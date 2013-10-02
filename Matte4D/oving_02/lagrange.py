'''
Created on 5. sep. 2012

@author: Habitats
'''

import numpy
import matplotlib.pyplot as plt
from math import *


def lagrange(points, fX, x):

    lagrangeLst = []
    for lx in range(len(points)):
        lk = 1.0
        for n in range(len(points)):
            if n != lx:
                lk *= (x - points[n]) / (points[lx] - points[n])
        lagrangeLst.append(lk)
    ans = 0.0
    for i in range(len(lagrangeLst)):
        ans += fX[i] * lagrangeLst[i]
    return ans
        
        
# prints out list with results
def lagrangeIntervall(points, fX, n):
    values = []
    x = points[0]
    for i in range(n):
        y = lagrange(points, fX, x)
        values.append([x, y])
        x += (points[-1] - points[0]) / (n - 1)
        
    return values
        
def plotFunc(points, fX, iter):
    for i in numpy.linspace(points[0], points[-1], iter):
        plt.plot(i, lagrange(points, fX, i), 'go')
        plt.plot(i, tan(i), 'bo')
    
    plt.ylim([-15.0, 15.0])
    plt.show()
    
def printFunc(fX,iter):
    print "printing results:"
    result = lagrangeIntervall(points, fX, iter)
    for x in result:
        print x
        
points = [-1.5, -0.75, 0, 0.75, 1.5]
fX = [-14.1014, -0.931596, 0, 0.931596, 14.1014]

#printFunc(fX,100)
plotFunc(points, fX, 200)






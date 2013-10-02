'''
Created on 5. sep. 2012

@author: Habitats
'''
from __future__ import division
from math import * 

def trapezoidal(func, x, b, steps):
    h = (b - x) / steps
    start = x
    end = b
    ans = 0.0
    
    for i in range(steps):
        if x == start or x == end:
            div = 0.5
        else:
            div = 1
        ans = ans + div * eval(func)
        x = x + abs(h) 
        
    return ans * h

print trapezoidal("exp(-x**2)", -1, 1, 500)

func, start, end, step = raw_input("func/from/too/step:\n").split(" ")

print 'evaluating: %s over the intervall [%s, %s] with step: %s' % (func, start, end, step)
print 'answer: %s' % trapezoidal(func, int(start), int(end), int(step))


'''
Created on 19. mai 2014

@author: Patrick
'''
from math import exp


def f(x):
    return 1 / (1 + exp(-x))

def df(x):
    return f(x) * (1 - f(x))

i1 = .35
i2 = .9

w11 = .1
w12 = .4

w21 = .8
w22 = .6

w13 = .3
w23 = .9

e1 = i1 * w11 + i2 * w21
o1 = f(e1)

e2 = i1 * w12 + i2 * w22 
o2 = f(e2)

e3 = o1 * w13 + o2 * w23 
o3 = f(e3)

print o1
print o2
print o3

t = .5

o = o3
delta = (t-o)*(1-o)*o

print delta

w13 = w13 + (delta * f(e3))
print w13
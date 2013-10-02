#! /usr/bin/env python
# itgk oeving 2

a = 24
b = 42
c = 64
f = 2
d = 2
e = f

def oppg2ab(): 
    if c > a and c > b:
        print '%d > %d og %d' % (c,a,b)
        print '%d og %d < %d' % (a,b,c)
    elif a < b:
        print '%d > %d og %d' % (b,a,c)
        print '%d og %d < %d' % (c,a,b)
    else:
        print '%d > %d og %d' % (a,c,b)
        print '%d og %d < %d' % (c,b,a)

def oppg2c():
    if f == 0:
        print '%d = 0; kan ikke dele med 0!' % f
    else:
        x = b/f
        print '%d / %d = %d' % (b,f,x)
        
def oppg2d():
    print '%d / %d = %d' % (a,d,a/d)
    print a/e # kan ikke dele med 0!

oppg2ab()
oppg2c()
oppg2d()

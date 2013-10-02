#! /usr/bin/env python
# itgk oeving 2.3c

import math

a = float(input('skriv inn et tall: '))
b = float(input('skriv inn et tall til: '))
c = float(input('og enda et..: '))


if b**2-4*a*c < 0:
    print 'likningen har ingen loesning!'
else:
    x = (-b-(math.sqrt(b**2-4*a*c)))/(2*a)
    y = (-b+(math.sqrt(b**2-4*a*c)))/(2*a) 
    if x == y:
        print 'likningen fikk en loesning: %d' % x
    else:
        print 'likningen har 2 gyldige loesninger: %d og %d' % (x,y)

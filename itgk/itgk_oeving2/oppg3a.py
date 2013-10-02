#! /usr/bin/env python
# itgk oeving 3a
 
number = input('Skriv inn et tall: ')

if number == 0:
    print '%d er null!' % number
elif number%2 == False:
    print '%d er et partall!' % number
else:
    print '%d er et oddetall!' % number

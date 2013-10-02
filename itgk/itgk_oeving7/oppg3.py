#! /usr/bin/env python
# itgk oeving 7 - oppg3

from random import randint 

def makeList():
    values = raw_input('').split(',')
    return [int(i) for i in values] 

def calcMassMid(lst):
    summed = sum(lst)
    half = 0
    x = 0
    while half <= summed/2.0:
        half = half + lst[x]
        x += 1
    print '%s index %s is the mass mid value' % (lst[x-1],x-1)

def randLst():
    x = []
    for i in range(0,randint(10,200)):
        x.append(randint(1,10))  
    print x
    return x

def run():
    print 'this script will find the balance point of list with positive ints'
    x = input('choose a script:\n 0 = enter a list in the format: x,x,x,x,x\n 1 = use a randomly generated list (length is 1 <= x <= 200, numbers 1 through 10)\n> ')
    if x == 1:
        calcMassMid(randLst())
    elif x == 0:
        calcMassMid(makeList())
    
run()
        


    


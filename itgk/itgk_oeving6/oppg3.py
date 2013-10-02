#! /usr/bin/env python
# itgk oeving 6 - oppg3

import math

def isPrime(x):
    if x <= 2:
        if x == 2:
            return True
        else:
            return False
    if x%2 == 0:
        return False
    for i in range(3,int(math.sqrt(x)+1)):
        if x%i == 0:
            return False
    else:
        return True

def check(x):
    if isPrime(x) == False:
        return 'not a prime'
    else:
        return 'is a prime'

def findPrime(x):
    y = []
    for i in range(0,x):
        if isPrime(i) == True:
            y.append(i)
    return y

def multipliers(x):
    y = []
    if isPrime(x) == True:
        return y
    else:
        for i in range(1,x):
            if x%i == 0:
                y.append(i)
        return y


# run stuff
def run():
    print 'choose a script'
    z = input('0 = check prime, 1 = find prime, 2 = find multipliers\n> ')

    if z == 0:
        print check(abs(input('enter a number to check if it\'s a prime\n> ')))
    elif z == 1:
        print findPrime(input('enter max value\n> '))
    elif z == 2:
        print multipliers(input('enter a number\n> '))
    else:
        run()
      
run()

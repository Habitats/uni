#! /usr/bin/env python
# itgk oeving 7 - oppg2

x = 4
def foo():
    x = 5
def bar():
    global x
    x = 5
print x # 4
foo()
print x # 4
bar()
print x # 5
def bar():
    global x
    x = 2
bar()
print x # 2

#############################

x = 4
def bar(x):
    y = 0
    print x # 4
    for x in range(0,10):
        y = x
    print x # 9, for loop does x += til, but not including 10
bar(x)
print x # 4

#############################

x = "4"
def bar(x):
    print x # '4' 
    for z in range(0,10):
        x = x + str(z)
    print x # '40123456789'
bar(x)
print x # '4'

#############################

from random import random 
print random() # 0 >= x >= 1
def random():
    return 4
print random() # 4

#############################

def foobar(y):
    x = y
    if x < 10:
        foobar(x+1)
    print x # 10,9,8...0, run function 10 times, then #10 finishes and prints 10, then #9 finish and prints 9... 
            # reverse: swap < with >, + with - and 10 with 0
foobar(0)

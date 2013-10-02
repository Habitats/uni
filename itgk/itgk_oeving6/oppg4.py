#! /usr/bin/env python
# itgk oeving 6 - oppg4

def calc(a,r,k):
    y = []
    for i in range(1,int(k)):
        v = a*(1+(r/12))**(12*i)
        y.append(v)
    return y

def sumInput(x):
    # convert str to floats
    y = [float(i) for i in x] 
    return calc(y[0],y[1],y[2])

# what's the minimal start value that'll achieve a specified end value
def minStart(endval):
    a = 1.0
    while endval > calc(a,0.05,20.0)[-1]: 
        a = a + 1000.0
    return a+1000

def run():
    print 'this program calculates the return on an investment subject to compound interest'
    x = input('choose a function: 0 = get a sum based on 3 values, 1 = enter a max value, and get minimum required start value\n> ')
    if x == 0:
        x = (raw_input('enter 3 values in the following format: startInput,interest,years\n> ').split(','))
        for i in sumInput(x):
            print int(round(i))
    elif x == 1:
        print int(minStart(input('enter the amount of money you intend to achive after 20 years with a fixed interest of 5%\n> ')))

run()

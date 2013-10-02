#! /usr/bin/env python
# Simple calculator

z = 0
x = float(input('Enter a number: '))
op = raw_input("Enter an operator: ")

if op == '+' or op == '-' or op == '/' or op == '*':

    y = float(input('Enter another number: '))

    if op == '+':
        z = x + y
        print "%d plus %d equals %d." % (x,y,z)
    elif op == '-':
        z = x - y
        print "%d minus %d equals %d." % (x,y,z)
    elif op == '*':
        z = x * y 
        print "%d times %d equals %d." % (x,y,z)
    elif op == '/':
        if y == 0:
            print "You cannot divide by zero you fool!"
            exit()
        else:
            z = x / y
            print "%d divided by %d equals %d." % (x,y,z)
    
    if z != int(z):
        print "The answer is %r, which is a decimal number." % z
    elif z % 2 == 0:
        print "The answer is %d, which is an even number." % z
    else:
        print "The answer is %d, which is an odd number." % z
     
else:
    print "Operator not recognized! Use one of the following: +, -, *, /"

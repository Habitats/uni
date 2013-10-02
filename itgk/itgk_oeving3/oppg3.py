#! /usr/bin/env python
# itgk oeving 3 - oppg3a

import math

scalarVar = []

def convertToInt(k):
    for i in range(len(k)):
        k[i] = int(k[i])

def vectorLength(k):
    return math.sqrt((k[0])**2+((k[1])**2)+((k[2])**2))

# prompt coords for a vector
vector = raw_input('enter 3 variables:\n> ').split(' ')

convertToInt(vector)

print 'length of vector %s is %r' % (vector,vectorLength(vector))

scalar = input('now enter a scalar:\n> ')

x = int(vector[0])*scalar
y = int(vector[1])*scalar
z = int(vector[2])*scalar

vectorScalar = [x,y,z] 
print 'length of vector %s is %r' % (vectorScalar,vectorLength(vectorScalar))

# prompt for a new vector
vector2 = raw_input('enter 3 new variables:\n> ').split(' ')

convertToInt(vector2)

for i in range(len(vector)):
    scalarVar.append(vector[i]*vector2[i])

scalarProd = scalarVar[0] + scalarVar[1] + scalarVar[2]

print 'the scalar product of %s dot %s is %r' % (vector,vector2,scalarProd)

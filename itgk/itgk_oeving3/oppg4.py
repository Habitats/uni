#! /usr/bin/env python
# itgk oeving 3 - oppg4

matOne = [] 
matTwo = []
matTree = []

def convertToInt(k):
    for i in range(0,3):
        k[i] = int(k[i])

def createMat(mat):
    rowOne = raw_input('enter 3 variables:\n> ').split(' ')
    rowTwo = raw_input('enter another 3 variables:\n> ').split(' ')
    rowTree = raw_input('enter another 3 variables:\n> ').split(' ')

    convertToInt(rowOne)
    convertToInt(rowTwo)
    convertToInt(rowTree)

    mat.append(rowOne)
    mat.append(rowTwo)
    mat.append(rowTree)

createMat(matOne)
createMat(matTwo)

print matOne
print matTwo

a = matOne[0][0]*matTwo[0][0] + matOne[0][1]*matTwo[1][0] + matOne[0][2]*matTwo[2][0]
b = matOne[0][0]*matTwo[0][1] + matOne[0][1]*matTwo[1][1] + matOne[0][2]*matTwo[2][1]
c = matOne[0][0]*matTwo[0][2] + matOne[0][1]*matTwo[1][2] + matOne[0][2]*matTwo[2][2]

d = matOne[1][0]*matTwo[0][0] + matOne[1][1]*matTwo[1][0] + matOne[1][2]*matTwo[2][0]
e = matOne[1][0]*matTwo[0][1] + matOne[1][1]*matTwo[1][1] + matOne[1][2]*matTwo[2][1]
f = matOne[1][0]*matTwo[0][2] + matOne[1][1]*matTwo[1][2] + matOne[1][2]*matTwo[2][2]

g = matOne[2][0]*matTwo[0][0] + matOne[2][1]*matTwo[1][0] + matOne[2][2]*matTwo[2][0]
h = matOne[2][0]*matTwo[0][1] + matOne[2][1]*matTwo[1][1] + matOne[2][2]*matTwo[2][1]
i = matOne[2][0]*matTwo[0][2] + matOne[2][1]*matTwo[1][2] + matOne[2][2]*matTwo[2][2]

matTree = [
        [a,b,c],
        [d,e,f],
        [g,h,i],
        ]

print matTree

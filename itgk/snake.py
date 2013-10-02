#! /usr/bin/env python
# snake examn

def createField(x):
    field = [[1 for i in range(x)] for i in range(x)] 

    # NEVRAR EVRAR
    #field = [[1]*x]*x
    #print field
    return field

def apples(field,apples):
    from random import randint,random

    # official way
    #n = len(field)
    #while apples > 0:
    #    x = int(random()*n)
    #    y = int(random()*n)
    #    if field[y][x] == 1:
    #        field[y][x] = 5
    #        apples -= 1
            
    # my way
    n = len(field)
    while apples > 0:
        x = randint(0,n)
        y = randint(0,n)

        if field[x][y] == 1:
            field[x][y] = 5
            apples -= 1

    #print field

def checkApple(field,x,y):
    if field[x][y] == 5:
        return True
    else:
        return False

def drawSnake(field,sX,sY):
    for i in range(len(sX)):
        field[sX[i]][sY[i]] = 0
    return field

def moveSnake(sX,sY,direction):
    if direction == 'r':
        sX[0] + 1
        sX.pop()
    elif direction == 'l':
        sX[0] - 1
        sX.pop()
    elif direction == 'd':
        sY[0] + 1
        sY.pop() 
    

x = 10
apples = 5
field = createField(x)
sX = [3,3,3,2,1]
sY = [2,3,4,4,4]

#apples(field,apples)
for i in drawSnake(field,sX,sY):
    print i

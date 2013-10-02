#! /usr/bin/env python
# the most amazing shit ever made (chess)

''' todo:
    - only allow pieces to move around on the actual board
    - only able to move pieces of own team
    - check if anything is blocking the path
    - knock out pieces
    - check for check 
    - check for checkmate
'''
from sys import stdout 
from pieces import *

# builds a list containing framework for indexes later used with a dict representing the field
def fieldCreate():
    # creates a basic 10*10 matrix
    field = [[i for i in range(10)] for i in range(10)]

    x = 0
    z = 0
    # inserts the coordinates for the playing field 
    for i in range(0,10):
        x = 0
        for j in range(0,10):
            field[i][j] = '%s%s' % (ltr[x],z)
            if x < 9:
                x += 1
            else:
                x = 0
        z += 1 

    return field

# insert standard values and layout
# and builds up a dict contaning coords as key and piece a value
def standardValues(fieldDict):
    for i in range(1,9):
    # vertial numbers
        fieldDict[field[i][9]] = ' %s ' % i
        fieldDict[field[i][0]] = ' %s ' % i
    # horizontal letters
        fieldDict[field[0][i]] = ' %s ' % ltr[i]
        fieldDict[field[9][i]] = ' %s ' % ltr[i]

    for i in range(1,9):
        for j in range(1,9):
            fieldDict[field[i][j]] = ' '*3
    # corners
    sep = ' * '
    fieldDict[field[9][9]] = sep 
    fieldDict[field[9][0]] = sep 
    fieldDict[field[0][0]] = sep 
    fieldDict[field[0][9]] = sep 

    # a key to store the amount of turns
    fieldDict['turns'] = 0

    # a key to store which team is next
    fieldDict['team'] = 'team1 (lower case)'

    return fieldDict

# fills up the board with pices in starting position
# by changing the value of the coord key
def startPos(fieldDict): 
    for i in range(1,9):
        fieldDict[field[1][i]] = team1[i]
        fieldDict[field[2][i]] = team1[8]
        fieldDict[field[8][i]] = team2[i]
        fieldDict[field[7][i]] = team2[8]

    # bugtesting
    fieldDict['d4'] = 'TOW'

def verify(old,new):
    # check if the new location is even on the board
    if fieldDict.has_key(new) != True:
        return False

    # check if the piece is trying to kick out one of its own
    if (fieldDict[new] in team1 and fieldDict[old] in team1) or (fieldDict[old] in team2 and fieldDict[new] in team2): 
        return False

    # split up the coords (a1,b4 etc) into numeric values (1,2,3...)
    x1,y1 = int(ltr.index(old[0])),int(old[1])
    x2,y2 = int(ltr.index(new[0])),int(new[1])

    # start testing if the new location is valid
    piece = fieldDict[old].lower()
    print piece
    if piece == 'kin' and king(x1,y1,x2,y2,fieldDict) == True:
        return True
    elif piece == 'que' and queen(x1,y1,x2,y2,fieldDict) == True:
        return True
    elif piece == 'paw' and pawn(x1,y1,x2,y2,fieldDict,fieldDict['team']) == True:
        return True
    elif piece == 'bis' and bishop(x1,y1,x2,y2,fieldDict) == True:
        return True
    elif piece == 'tow' and tower(x1,y1,x2,y2,fieldDict) == True:
        return True
    elif piece == 'kni' and knight(x1,y1,x2,y2,fieldDict) == True:
        return True
    else:
        return False

# move pieces
def move(fieldDict,old,new):
    fieldDict[new] = fieldDict[old]
    fieldDict[old] = '   '
    fieldDict['turns'] += 1
    if fieldDict['turns'] % 2 == 0:
        fieldDict['team'] = 'team1 (lower case)'
    else:
        fieldDict['team'] = 'team2 (upper care)'
        
    # i have no idea why i don't seem to need this
    #return fieldDict

# print it pretty
def printField(fieldDict):
    clear()
    print '\nthe amazing superfantasic chess adventure\n - by habitats'
    print '\n - 1. restart/clear the board\n - 2. new game'
    print '-'*41
    x = 0
    for i in field:
        for j in i:
            if x < 9:
                # use this instead of print to get everything on one line
                stdout.write('|%s' % fieldDict[j]) 
                stdout.flush()
                x += 1
            else:
                print '|%s|' % fieldDict[j]
                x = 0
            
        print '-'*41
    print 'turns: %s' % fieldDict['turns'] 
    print 'next up: %s' % fieldDict['team']

def play():
    # ask for from and to values
    try:
        old,new = raw_input('\nfrom,to:\n> ').split(',')
    except ValueError:
        print 'error: invalid coordinates'
        play()
    try:
        if verify(old,new) == True:
            # move a piece
            move(fieldDict,old,new)
            printField(fieldDict)
            print 'system: moved a %s from %s to %s' % (fieldDict[new],old,new)
        else:
            print 'error: what the actual fuck are you doing?!'
    except ValueError:
        print 'error: invalid coordinates'
        play()
    play()

def restart():
    return printField((standardValues(fieldDict)))

# clears the screen for a smooth experience
def clear():
    import os
    os.system(['clear','cls'][os.name == 'nt'])

def run():
    restart()
    printField(fieldDict)
    try:
        choice = int(raw_input('> '))
    except ValueError:
        print 'error: invalid option'

    if choice == 1:
        restart()
        run()
    elif choice == 2:
        restart()
        startPos(fieldDict)
        printField(fieldDict)
        play()

# define stuff

ltr = 'zabcdefghi'
cmd = str()
fieldDict = {}
turns = 0
field = fieldCreate()
team1 = ['TOW','KNI','BIS','QUE','KIN','BIS','KNI','TOW','PAW']
team2 = ['tow','kni','bis','que','kin','bis','kni','tow','paw']

# run stuff

clear()
run()

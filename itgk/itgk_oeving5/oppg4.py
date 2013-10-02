#! /usr/bin/env python
# itgk oeving 5 - oppg4e

import random

def randomRoom(safe,trap,hole):
    room = [0,0,0,0]
    doors = random.randint(1,4)
    t = random.randint(1,doors)
    room[t-1] = safe
    for i in range(1,doors+1):
        r = random.randint(1,2)
        if not i == t:
            if(r == 1):
                room[i-1] = trap
            else:
                room[i-1] = hole
    return room

def lagcave():
    cave = []
    ant = input('how many rooms do you wan\'t you want to play with?\n> ')
    
    for i in range(0,ant-1):
        cave.append(randomRoom('T','F','B'))
    cave.append(randomRoom('M','F','B'))
    return cave

def tryRoom(roomnr,rooms):
   
    room = rooms[roomnr]
    print 'this room has %d doors' % (len(room) - room.count(0))
    if not checkDoor(room):
        tryRoom(roomnr+1,rooms)
    
def checkDoor(room):
    door = input('enter the doornr. you want to check\n> ')
    neste = room[door -1]
    if(neste == 'T'):
        print 'there\'s a safe room behind this door'
        print 'you enter the next room'
        return False
    elif neste == 'B':
        print 'there\'s a bottomless pit behind this door!'
        checkDoor(room)
    elif neste == 'F':
        print 'there\'s a trap behind this one! try another one!'
        checkDoor(room)
    else:
        print 'the game, you won!'
        return True
caveMap = lagcave()

tryRoom(0,caveMap)

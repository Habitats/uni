#! /usr/bin/env python
# defines how the chess pieces may move around

def king(x1,y1,x2,y2,fieldDict):
    if abs(x1-x2) > 1 or abs(y1-y2) > 1:
        return False
    else:
        return True

def queen(x1,y1,x2,y2,fieldDict):
    return True 

# need to add code for pushing over shit
def pawn(x1,y1,x2,y2,fieldDict,team):
    #if fieldDict['%s%s' % (x1+1,y1+1)] != '   ' or fieldDict['%s%s' % (x1-1,y1+1)] != '   ':
    #    print 'durrrr'
    if y1 == 2 or y1 == 7:
        x = 2
    else:
        x = 1
    if x1 != x2:
        return False
    if '1' in team:
        if 0 <= y1-y2 <= x:
            return True 
    if '2' in team:
        if 0 <= y2-y1 <= x:
            return True 
    else:
        return False
    
def bishop(x1,y1,x2,y2,fieldDict):
    if x1-x2 != y1-y2: 
        return False

def tower(x1,y1,x2,y2,fieldDict):
    if (x1 != x2 and y1 == y2) or (x1 == x2 and y2 != y1):
        return True 
    else:
        return False 

def knight(x1,y1,x2,y2,fieldDict):
    if (abs(x1-x2) == 1 and abs(y1-y2) == 2) or (abs(x1-x2) == 2 and abs(y1-y2) == 1):
        return True
    else:
        return False 

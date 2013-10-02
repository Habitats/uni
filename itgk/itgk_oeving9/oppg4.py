#! /usr/bin/env python
# itgk oeving 9 - oppg4

def matCreate(f):
    f = open(f,'r')
    mat = [[None for i in range(8)] for j in range(5)]
    x = 0
    for i in f.readlines():
        for j in range(8):
            mat[x][j] = stripper(i.split(',')[j])
        x += 1
    f.close()
    return mat

def stripper(x):
    y = str() 
    for i in x:
        if i.isalpha():
                y = y+i
    return y

def setTime(mat,day,time,course):
    matDict = {
            '0800':0,'monday':0,
            '0900':1,'tuesday':1,
            '1000':2,'wedensday':2,
            '1100':3,'thursday':3,
            '1200':4,'friday':4,
            '1300':5,
            '1400':6,
            '1500':7,
            }
    try:
        mat[matDict[day]][matDict[time]] = course
    except KeyError:
        print 'not a valid time argument'
        return
    matWrite(mat)
    print 'added shit'
    return mat

def matWrite(mat):
    f = open('timeplan','w')
    for i in mat:
        for j in range(len(i)):
            if j == len(i)-1:
                f.write('%s,\n' % i[j])
            else:
                f.write('%s,' % i[j])
    f.close()

def printMat(mat):
    f = open('timeplan','r')
    for i in f.readlines():
        print i

def run():
    try:
            mat = matCreate('timeplan')
    except IndexError:
        print 'something fucked up'
    print '\nwelcome to awesomesauce timeplan-organizer'
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '1. view timeplan'
    print '2. add shit'
    print '0. to quit'
    choice = input('> ')
    if choice == 0:
        import sys
        sys.exit('so long sucker')
    elif choice == 1:
        printMat(mat)
    elif choice == 2:
        day,time,course = raw_input('enter day, time and course:\n> ').split(',')
        setTime(mat,day,time,course)
    run()
    

run()


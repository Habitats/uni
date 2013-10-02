#! /usr/bin/env python
# itgk oeving 9 - oppg2


def countLines(x):
    f = open(x,'r')
    output =  len(f.readlines())
    f.close()
    return output 

def countNum(x):
    countDict = {}
    f = open(x,'r')

    for i in list(f.read()):
        if i.isdigit():
            countDict[i] = countDict.get(i,0) + 1 

    f.close()
    return countDict
 
def formatOutput(x):
    f = open('test','w')
    for i in range(len(x)):
        f.write('%s occurs %s time(s)\n' % (x.keys()[i],x.values()[i]))
    f.close()
        
fileName = 'exercise2.txt'

formatOutput(countNum(fileName))

            


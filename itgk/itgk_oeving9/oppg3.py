#! /usr/bin/env python
# itgk oeving 9 - oppg3

def createDict(x):
    f = open(x,'r')
    dic = {}

# creates a dictionary with courses as key and requirement as value
    for i in f.readlines():
        try:
            dic[i.split('",')[0]] = i.split('",')[1] 
        except IndexError:
            pass
    return dic

def convertDict(dic,y,z):
# removes all but entries containing 'Alle' as value if y = 0
    for i in dic.copy():      
        if y == 0:
            if 'Alle' not in dic[i]:
                del dic[i]
# removes all but entries containing a digit value if y != 0
        elif y == 1:
            try:
                float(dic[i])
            except ValueError:
                del dic[i]
# optional uni filter
    if z != None:
        for i in dic.keys():
            if str(z) not in i:
                del dic[i]
    if len(dic) < 1:       
        import sys
        sys.exit('no such university!')
    else:
        return (dic,z)

# calulates the average limit min and max
def average(x,uni):
    if uni == 0:
        uni = 'total'
    total = 0
    for i in x.values():
        total += float(i)
    average = total/float(len(x))
    return '%s: average: %s' % (uni,average)

def minLim(x,uni):
    if uni == 0:
        uni = 'total'
    z = 100
    pos = 0
    for i in x:
        if float(x[i]) < z: 
            z = float(x[i])
            pos = i
    return '%s: minimum: %s at "%s"' % (uni,fullDict[pos][:-1],pos[1:])


def maxLim(x,uni):
    if uni == 0:
        uni = 'total'
    z = 0
    pos = 0
    for i in x:
        if float(x[i]) > z: 
            z = float(x[i])
            pos = i
    return '%s: highest: %s at "%s"' % (uni,fullDict[pos][:-1],pos[1:])


# define shit
filename = 'poenggrenser_2011.csv'
uni = raw_input(' score requirement calculator\n enter the school you want to check (NTNU, UIO, HIA etc) OR leave it blank for total\n> ')

fullDict = createDict(filename)

(allDict,uni) = convertDict(fullDict.copy(),0,uni)
(limDict,uni) = convertDict(fullDict.copy(),1,uni)

# run shit
print average(limDict,uni)
print maxLim(limDict,uni)
print minLim(limDict,uni)


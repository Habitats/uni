#! /usr/bin/env python     
# read file description (ie. 2. line of every file)

import linecache
import os, fnmatch # for recursively searching for *.py

files = []
fileDict = {}
filenameClean = []

def check():
    for root, dirnames, filenames in os.walk('/home/bullshit/python/'):
        for filename in fnmatch.filter(filenames, '*.py'):
            files.append(os.path.join(root, filename))
            fileDict[filename] = os.path.join(root, filename)
    print """
 - Name - Description
 -------------------------------------------------------------------------- """

def sortPrint():
    sortedTups = sorted(fileDict.items())
    lenght =  maxLenght(sortedTups)
    for x in sortedTups:
        desc = linecache.getline(x[1],2)
        print " - %s%s - %s" % (x[0],whiteSpace(x[0],lenght),desc[2:(len(desc)-2)]) 

def run():
    print '\n>> Pick a file you want to run.'
    name = raw_input(' > ')
    durp = fnmatch.filter(fileDict,'*%s*' % name)
    try:
        execfile(fileDict[durp[0]])
    except Exception,err:
        if len(durp) == 0:
            print ">> File not found..."
        else:
            print ">> Error in file: %s" % err
        run() 

# finds max lenght of string by comparing with the next one. if 'max1 > max2', keep max2
# 'array_to_check' is a list of 'key value pairs'; hence [0] 
def maxLenght(array_to_check):
    lenght = 0
    for y in array_to_check:
        if len(y[0]) > lenght:
            lenght = len(y[0])
    return lenght

def whiteSpace(string,lenght):
    z = lenght - len(string)
    a = ''
    for i in range(0,z):
        a = ' ' + a
    return a
 
check()
sortPrint()
run()

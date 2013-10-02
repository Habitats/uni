'''
Created on 28. aug. 2012

@author: Habitats
'''

from random import randint
from time import time

size = 300

lst = [None] * size

for i in range(len(lst)):
    lst[i] = chr(randint(33, 126))
#print lst

def concatination():
    randSeq = "" 
    for i in lst:
        randSeq += i;
    return randSeq

def joining():
    randLst = []
    for i in lst:
        randLst.append(i)
    return ''.join(randLst);

start = time()
print len(concatination())
print "Concatination: ", time() - start 

start = time()
print len(joining())
print "Joining: ", time() - start


map = {}

map['1'] = "sup"
map['4'] = "sup"
map['6'] = "sup"
map['2'] = "sup"

print sorted(map)

print map

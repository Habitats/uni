'''
Created on 29. aug. 2012

@author: Habitats
'''

from random import randrange
from time import time

def closeRelations(seq):
    dd = float("inf")
    for x in seq:
        for y in seq:
            if x == y:
                continue
            d = abs(x - y)
            if d < dd:
                xx, yy, dd = x, y, d
    return xx, yy
        
        
            
def closeRelationsSort(seq):
    seq.sort()
    dd = float("inf")
    for i in range(len(seq) - 1):
        x , y = seq[i], seq[i + 1]
        if x == y:
            continue
        d = abs(x - y)
        if d < dd:
            xx, yy, dd = x, y, d
    return xx, yy


seq = [randrange(10 ** 10) for i in range(1000000)]

start = time()
#closeRelations(seq)
print time() - start

start = time()
closeRelationsSort(seq)
print time() - start


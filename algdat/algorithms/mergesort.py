'''
Created on 29. aug. 2012

@author: Habitats
'''
import random

def mergesort(seq):
    global cnt
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1:
        lft = mergesort(lft)
    if len(rgt) > 1:
        rgt = mergesort(rgt)
    res = []
    while lft and rgt: 
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
        cnt += 1
    res.reverse()
    return (lft or rgt) + res

cnt = 0
seq = [random.randrange(0, 100) for n in range(5)]

#print seq
seq = mergesort(seq)
print "random (avergae):"
print cnt
cnt = 0

seq.reverse()
#print seq
seq = mergesort(seq)
print "worst:"
print cnt

cnt = 0
seq = mergesort(seq)
#print seq
print "best:"
print cnt

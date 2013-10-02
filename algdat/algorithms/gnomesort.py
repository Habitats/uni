'''
Created on 29. aug. 2012

@author: Habitats
'''
import random

def gnomesort(seq, rev):
    i = 0
    cnt = 0
    while i < len(seq):
        if i == 0 or seq[i - 1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i - 1] = seq[i - 1], seq[i]
            i -= 1
        cnt += 1
    if rev:
        seq.reverse()
    return (seq, cnt)

#seq = [1, 3, 56, 123, 5, 6, 1, 34, 41, 72, 0, 1234, 45, 56, 45, 234, 234]
seq = [random.randrange(0, 100) for n in range(1000)]

print "sequence:"
print seq

print "random (averge):"
seq, cnt = gnomesort(seq, 1)
#print seq
print cnt, "iterations"

print "worst:"
seq, cnt = gnomesort(seq, 0)
#print seq
print cnt, "iterations"

print "best:"
seq, cnt = gnomesort(seq, 0)
#print seq
print cnt, "iterations"

        

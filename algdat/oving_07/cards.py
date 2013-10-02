'''
Created on 15. okt. 2012

@author: Habitats
'''

from sys import stdin
from itertools import repeat
import copy
import collections

def mergeTweak(decks):
    # SKRIV DIN KODE HER
    def mergesort(seq):
        mid = len(seq) // 2
        lft, rgt = seq[:mid], seq[mid:]
        if len(lft) > 1:
            lft = mergesort(lft)
        if len(rgt) > 1:
            rgt = mergesort(rgt)
        res = []
        while lft and rgt: 
            if lft[-1][0] >= rgt[-1][0]:
                res.append(lft.pop())
            else:
                res.append(rgt.pop())
        res.reverse()
        return (lft or rgt) + res
    
#    lst = []
#    for i in decks:
#        lst += i
    
#    sorted = mergesort(decks)
#    
    res = []
#    for i in sorted:
#        res.append(i[0]][-1])
    
    return "".join(res)
    
def merganizer(decks):
    
    def merger(lft, rgt):
        res = []
        while lft and rgt:
            if lft[-1][0] >= rgt[-1][0]:
                res.append(lft.pop())
            else:
                res.append(rgt.pop())
        res.reverse()
        return (lft or rgt) + res
    
    res = []
    while decks:
        if not res and len(decks) > 1:
            lft = decks.pop()
            rgt = decks.pop()
            res = merger(lft, rgt)
            
        elif len(decks) is 10:
            lft = decks.pop()
            rgt = decks.pop()
            res1 = merger(lft, rgt)
            
            lft = decks.pop()
            rgt = decks.pop()
            res2 = merger(lft, rgt)
            
            lft = decks.pop()
            rgt = decks.pop()
            res3 = merger(lft, rgt)
            
            lft = decks.pop()
            rgt = decks.pop()
            res4 = merger(lft, rgt)
            
            lft = decks.pop()
            rgt = decks.pop()
            res5 = merger(lft, rgt)
            
            res6 = merger(res1, res2)
            res7 = merger(res3, res4)
            res8 = merger(res5, res6)
            res9 = merger(res7, res8)
            
            res = merger(res9, res)
        elif len(decks) is 9:
            lft = decks.pop()
            rgt = decks.pop()
            res1 = merger(lft, rgt)
            
            lft = decks.pop()
            rgt = decks.pop()
            res2 = merger(lft, rgt)
            
            lft = decks.pop()
            rgt = decks.pop()
            res3 = merger(lft, rgt)
            
            lft = decks.pop()
            rgt = decks.pop()
            res4 = merger(lft, rgt)
            
            lft = decks.pop()
            res5 = merger(res1, res2)
            res6 = merger(res3, res4)
            res7 = merger(res5, res6)
            
            res8 = merger(lft, res7)
            
            res = merger(res8, res)
        elif len(decks) is 8:
            lft = decks.pop()
            rgt = decks.pop()
            res1 = merger(lft, rgt)
            
            lft = decks.pop()
            rgt = decks.pop()
            res2 = merger(lft, rgt)
            
            lft = decks.pop()
            rgt = decks.pop()
            res3 = merger(lft, rgt)
            
            lft = decks.pop()
            rgt = decks.pop()
            res4 = merger(lft, rgt)
            
            res5 = merger(res1, res2)
            res6 = merger(res3, res4)
            res7 = merger(res5, res6)
            
            res = merger(res7, res)
        elif len(decks) is 7:
            lft = decks.pop()
            rgt = decks.pop()
            res1 = merger(lft, rgt)
            
            lft = decks.pop()
            rgt = decks.pop()
            res2 = merger(lft, rgt)
            
            lft = decks.pop()
            rgt = decks.pop()
            res3 = merger(lft, rgt)
            
            lft = decks.pop()
            res4 = merger(res3, lft)
            
            res5 = merger(res1, res2)
            res6 = merger(res5, res4)
            
            res = merger(res6, res)
        elif len(decks) is 6:
            lft = decks.pop()
            rgt = decks.pop()
            res1 = merger(lft, rgt)
            
            lft = decks.pop()
            rgt = decks.pop()
            res2 = merger(lft, rgt)
            
            lft = decks.pop()
            rgt = decks.pop()
            res3 = merger(lft, rgt)
            
            res4 = merger(res1, res2)
            res5 = merger(res4, res3)
            
            res = merger(res5, res)
        elif len(decks) is 5:
            lft = decks.pop()
            rgt = decks.pop()
            res1 = merger(lft, rgt)
            
            lft = decks.pop()
            rgt = decks.pop()
            res2 = merger(lft, rgt)
            
            lft = decks.pop()
            res3 = merger(res1, res2)
            res4 = merger(lft, res3)
            
            res = merger(res4, res)
        elif len(decks) is 4:
            lft = decks.pop()
            rgt = decks.pop()
            res1 = merger(lft, rgt)
            
            lft = decks.pop()
            rgt = decks.pop()
            res2 = merger(lft, rgt)
            
            res3 = merger(res1, res2)
            res = merger(res3, res)
            
        elif len(decks) is 2:
            lft = decks.pop()
            rgt = decks.pop()
            res2 = merger(lft, rgt)
            res = merger(res2, res)
            
        elif len(decks) > 0:
            res = merger(decks.pop(), res)
    
    letters = []
    for i in res:
        letters.append(i[1])
    
    return "".join(letters)
            
    
            
def merge(decks):
    # SKRIV DIN KODE HER
    sorted = []
    
    j = 0
    while decks:
        i = 0
        max = -1
        while i < len(decks):
            if not len(decks[i]):
                decks.pop(i)
                continue
            value = decks[i][-1][0]
            if max < value:
                max = value 
                j = i
            i += 1
        if not decks:
            return "".join(reversed(sorted))
        sorted.append(decks[j].pop()[1])
    return "".join(reversed(sorted))
    
def run():
    decks = []
#    def derp():
#        for line in stdin:
#            (index, list) = line.split(':')
#            deck = zip(map(int, list.split(',')), repeat(index))
#            decks.append(deck)
    def herp():
        input = [ "i:1", "n:2", "t:0", "a:6", "v:9"]
        input = ["c:688446720", "b:0", "k:950908367", "q:1062913590", "p:269124576", "s:405974318" ] 
        for line in input:
            (index, list) = line.split(':')
            deck = zip(map(int, list.split(',')), repeat(index))
            decks.append(deck)
#    derp()
    herp()
#    print merge(decks)
#    herp()
    print merganizer(decks)
#    herp()
#    print mergeTweak(decks)

run()

'''
Created on 7. okt. 2012

@author: Habitats
'''

from sys import stdin

def mergesort(seq):
    # Merk: den sorterte lista ma returneres
    # SKRIV DIN KODE HER
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
    res.reverse()
    return (lft or rgt) + res

def finn(sorted, nedre, ovre):
    # Merk: resultatet ma returneres
    # SKRIV DIN KODE HER
    limits = [None] * 2
    for i in sorted:
        if i <= nedre:
            limits[0] = i
        if i >= ovre:
            limits[1] = i
            break
    if limits[1] == None:
        limits[1] = sorted[-1]
    if limits[0] == None:
        limits[0] = sorted[0]
    
    return limits

def run():
    liste = []
#    liste = [12, 90, 5, 18, 140, 130, 143, 70]
    if not liste:
        for x in stdin.readline().split():
            liste.append(int(x))
    
    sortert = mergesort(liste)
    
    for linje in stdin:
        ord = linje.split()
        minst = int(ord[0])
        maks = int(ord[1])
        resultat = finn(sortert, minst, maks)
        print str(resultat[0]) + " " + str(resultat[1])

run()

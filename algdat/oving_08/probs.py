'''
Created on 23. okt. 2012

@author: Habitats
'''
from sys import stdin, stderr
from math import log

def beste_sti(nm, sans):
    # SKRIV DIN KODE HER
    
    n = len(nm)
    pre = [[0 for i in range(n)] for i in range[n]]
    paths = []
    print 
    for i in range(n):
        for j in range(n):
            if nm[i][j]:
                nm[i][j] = sans[j] 
    
    for node in range(n):
        for i in range(n):
            for j in range(n):
                
    
    
    floyd = [row for row in nm]
    n = len(floyd)
    D0 = floyd
    for k in range(n):
        Dk = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
#                Dk[i][j] = min(D0[i][j], D0[i][k] + D0[k][j])
                Dk[i][j] = min(log(sans[j]) + log(sans[i]), log(sans[j]) + log(sans[k]) + log(sans[k]) +log( sans[j])
#            for row in Dk:
#                print row 
                
    for row in Dk:
        print row 


def run():
    nabomatrise = []
    input = []
    input = ["6", "1.0 0.9 0.3 0.1 0.8 1.0", "1 2", "0 3 4", "0 3 4", "1 2 5", "1 2 5", "3 4"] 
    if not input:
        input = stdin
        n = int(input.readline())
        sansynligheter = [float(x) for x in input.readline().split()]
    else:
        n = int(input.pop(0))
        sansynligheter = [float(x) for x in input.pop(0).split()]
        
    for linje in input:
        naborad = [0] * n 
        naboer = [int(nabo) for nabo in linje.strip().split()]
        for nabo in naboer:
            naborad[nabo] = 1
        nabomatrise.append(naborad)
        print linje
    print beste_sti(nabomatrise, sansynligheter)

run()

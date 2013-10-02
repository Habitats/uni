'''
Created on 24. sep. 2012

@author: Habitats
'''

from sys import *
import traceback


def traverse(node, nabomatrise, startnode, visited, done):
    for i in range(len(node)):
        if node[i] == True:
            visited.append(i)
    done.add(startnode)
    for j in visited:
        if j in done:
            continue
        traverse(nabomatrise[j], nabomatrise, j, visited, done)
    return done
        

def subgraftetthet(nabomatrise, startnode):
    n = len(nabomatrise)
    # SKRIV DIN KODE HER
    nodes = set(range(n))
    
    node = nabomatrise[int(startnode)];
    reachableNodes = traverse(node, nabomatrise, startnode, visited=[], done=set())
        
    unreachableNodes = nodes.difference(reachableNodes)
    
#    print "reachable: ", reachableNodes
#    print "unreachable: ", unreachableNodes
    
    edges = set()
    
    print edges
    for i in unreachableNodes:
        node = nabomatrise[i]
        for j in range(len(node)):
            if node[j] == True and j in unreachableNodes:
#                if node.index(j) not in reachableNodes:
                edges.add((i, j))
    print edges
    
    numEdges = len(edges)
    numNodes = len(unreachableNodes)
    
#    print "edges: " , numEdges
#    print "nodes: ", numNodes
        
    if numNodes == 0:
        return 0.0
    else:
        return float(numEdges) / float(numNodes ** 2)


import fileinput

def fromCode():
    input = []
    for line in fileinput.input():
        input.append(line)
#    input = ["6", "011000", "000100", "000110", "000001", "010101", "000100", "3", "2", "3", "4", "5"] 
    n = int(input.pop(0))
    nabomatrise = [None] * n
    for i in range(0, n):
        nabomatrise[i] = [False] * n
        linje = input.pop(0)
        for j in range(0, n):
            nabomatrise[i][j] = (linje[j] == '1')
            
    for linje in input:
        start = int(linje)
        print "%.3f" % (subgraftetthet(nabomatrise, start) + 1E-12)
    

def fromInput():
    try:
        n = int(stdin.readline())
        nabomatrise = [None] * n # rader
        for i in range(0, n):
            nabomatrise[i] = [False] * n # kolonner
            linje = stdin.readline()
            for j in range(0, n):
                nabomatrise[i][j] = (linje[j] == '1')
        for linje in stdin:
            start = int(linje)
            print "%.3f" % (subgraftetthet(nabomatrise, start) + 1E-12)
    except:
        traceback.print_exc(file=stderr)

#print 
fromInput()
#fromCode()

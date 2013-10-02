'''
Created on 26. sep. 2012

@author: Habitats
'''

from heapq import heappop, heappush
from fileinput import input

def prim(graph, startNode):
    minimalSpanTree, heapQueue = {} , [(0, None, startNode)] # weight - lastNode - startNode
    maxWeight = 0
    weights = []
    while heapQueue:
        nodeWeight, lastNode, newNode = heappop(heapQueue)
        if newNode in minimalSpanTree: 
            continue
        minimalSpanTree[newNode] = lastNode
        if nodeWeight > maxWeight:
            maxWeight = nodeWeight
        for node, weight in graph[newNode].items():
#            print "from:", node , "to:" , newNode, "weight:" , weight
            heappush(heapQueue, (weight, newNode, node))
    
    return maxWeight
#    return minimalSpanTree,maxWeight
        
linjer = ["1:5 2:3 3:7", "0:5 3:1", "0:3", "0:7 1:1"]

linjer = [
         {1:5, 2:3, 3:7},
         {0:5, 3:1},
         {0:3},
         {0:7, 1:1}
         ]
        
def genInput():
    for line in input():
        print line
    
genInput()
print prim(linjer, 0)

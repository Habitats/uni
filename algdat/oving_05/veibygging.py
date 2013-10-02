'''
Created on 26. sep. 2012

@author: Habitats
'''

from heapq import heappop, heappush
from fileinput import input
#import time

def prim(graph):
    minimalSpanTree, heapQueue = {} , [(0, None, 0)] # weight - lastNode - startNode
    maxWeight = 0
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
        
def genInput():
    graph = []
    node = 0
    for line in input():
        args = line.split() 
        node = {}
        for arg in args:
            to, weight = arg.split(":")
            to = int(to)
            weight = int(weight)
            node[to] = weight
        graph.append(node)
    return graph

#start = time.clock()
#graph = genInput()
#print (time.clock() - start) * 1000
#
#start = time.clock()
#print prim(graph, 0)
#print (time.clock() - start) * 1000

#start = time.clock()
print prim(genInput())
#print time.clock()-start

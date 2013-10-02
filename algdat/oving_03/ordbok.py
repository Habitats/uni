'''
Created on 13. sep. 2012

@author: Habitats
'''


from sys import stdin, stderr
import traceback

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

def bygg(ordliste):
    toppNode = Node()
    toppNode.posi = 0
    
    for i in range(len(ordliste)):
        addNode(toppNode, 0, ordliste[i][0], ordliste[i][1])
        
    return toppNode

def addNode(parentNode, index, word, posi):
    if index == len(word)  : return
    
#    print "index:" , index , "posi:", posi, "word:" , word , "letter:"  , word[index] , "keys:" , parentNode.barn.keys()
    
    if word[index] in parentNode.barn.keys():
        childNode = parentNode.barn[word[index]]
    else: 
        childNode = Node()
        
    if index == len(word) - 1:
        childNode.posi.append(posi)
    parentNode.barn[word[index]] = childNode
    addNode(childNode, index + 1, word, posi)
    



def posisjoner(ord, index, node):
    if index == len(ord): return node.posi
    
    if node.barn.has_key(ord[index]):
        childNode = node.barn[ord[index]]
        return posisjoner(ord, index + 1, childNode)
    if ord[index] == "?":
        res = []
        index += 1
        for childNode in node.barn.values():
            res += posisjoner(ord, index, childNode)
        return res
        
    return []


def fromCode():
    input = [
    "ha ha mons har en hund med moms hun er en hunn",
    "ha",
    "mons",
    "hun",
    "mjau",
    "m?d",
    "e?"]
    ord = input[0].split()
    ordliste = []
    pos = 0
    for o in ord:
        ordliste.append((o, pos))
        pos += len(o) + 1
    
    toppnode = bygg(ordliste)
    
    for i in range(1, len(input)):
        sokeord = input[i]
        print sokeord + ":",
        posi = posisjoner(sokeord, 0, toppnode)
        posi.sort()
        for p in posi:
            print p,
        print
    
def fromFile():
    try:
        ord = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in ord:
            ordliste.append((o, pos))
            pos += len(o) + 1
        toppnode = bygg(ordliste)
        for sokeord in stdin:
            sokeord = sokeord.strip()
            print sokeord + ":",
            posi = posisjoner(sokeord, 0, toppnode)
            posi.sort()
            for p in posi:
                print p,
            print
    except:
        traceback.print_exc(file=stderr)
        
fromCode()
#fromFile()
    
    

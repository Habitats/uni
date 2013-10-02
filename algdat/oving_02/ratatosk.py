from sys import stdin
from compiler.misc import Stack

# var ikke definert i den gamle python-versjonen som 
# ligger paa noen av stud sine maskiner
True = 1
False = 0

class Node:
    barn = None 
    ratatosk = None
    visited = None # bare til bruk i DFS
    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.visited = 0
        self.level = 0

def dfs(rot):
    nodes = Stack()
    if rot.ratatosk: return 0
    nodes.push(rot)
    visited = []
    add = True
    
    while nodes:
        lastNode = nodes[-1]
        if lastNode.barn:
            childNr = 0
            while lastNode.barn[childNr] in visited:
                if childNr == len(lastNode.barn) - 1:
                    visited.append(nodes.pop())
                    add = False
                    break
                childNr += 1
                add = True
            child = lastNode.barn[childNr]
            if child.ratatosk: return len(nodes)
            if add:
                nodes.push(child)
            continue
        visited.append(nodes.pop())
    
    
from collections import deque
def bfs(rot):
    # SKRIV DIN KODE HER
    que = deque()
    node = rot
    pop = que.popleft
    append = que.append
    
    while(not  node.ratatosk):
        for barn in node.barn:
            barn.level = node.level + 1
            append(barn)
        
        node = pop()
    
    return node.level
                
                
## from code
#funksjon = "dfs" 
#antall_noder = int(10)
#noder = []
#
#for i in range(antall_noder):
#    noder.append(Node())
#start_node = noder[0]
#ratatosk_node = noder[5]
#ratatosk_node.ratatosk = True
#
#linjer = ["7 8 9", "1 4 5", "3 6 7", "0 1 2 3"]
#for linje in linjer:
#    tall = linje.split()
#    temp_node = noder[int(tall.pop(0))]
#    for barn_nr in tall:
#        temp_node.barn.append(noder[int(barn_nr)])
        
# from file
def start():

    funksjon = stdin.readline().strip()
    antall_noder = int(stdin.readline())
    noder = []
    for i in range(antall_noder):
        noder.append(Node())
    start_node = noder[int(stdin.readline())]
    ratatosk_node = noder[int(stdin.readline())]
    ratatosk_node.ratatosk = True
    for linje in stdin:
        tall = linje.split()
        temp_node = noder[int(tall.pop(0))]
        for barn_nr in tall:
            temp_node.barn.append(noder[int(barn_nr)])

    if funksjon == 'dfs':
        print dfs(start_node)
    elif funksjon == 'bfs':
   
        print bfs(start_node)
    elif funksjon == 'velg':
        print bfs(start_node)
start()
    
    
    

import heapq, time
from sets import Set
from collections import deque

x = "x"
o = "o"
sep = "-"  # sep
teams = x, o

class Node(object):
    state = None
    h = None
    g = None
    f = None

    children = None
    parent = None

    id = None

    def __init__(self, state, parent = None):
        self.state = state
        self.parent = parent
        self.children = []
        if parent != None:
            self.g = parent.g + 1
            parent.children.append(self)
        else:
            self.g = 0

        self.genId()

    def heuristic(self, state, goal):

        def hSingleTeam(state, goal, team):
            h = 0
            while(team in state):
                indexState = state.index(team)
                indexGoal = goal.index(team)
                h += abs(indexState - indexGoal)
                state.pop(indexState)
                goal.pop(indexGoal)
            return h

        # state = [x,x,x,-,0,0,0]
        # goal  = [0,0,0,-,x,x,x]
        h = 0
        for team in teams:
            h += hSingleTeam(list(state), list(goal), team)
#        print state, h
        return h

    def genId(self):
        self.id = ''.join(self.state)

    def genHeuristic(self, goal):
        self.h = self.heuristic(self.state, goal)

    def genDistanceFromRoot(self):
        g = 0
        node = self
        while(node.parent):
            node = node.parent
            g += 1
        self.g = g

    # for sorting (comparator)
    def __lt__(self, other):
        return self.f < other.f

def solutionSet(node):
    solution = []
    solutionSet = Set()
    while(node.parent):
        solution.append(node.state)
        solutionSet.add(node.id)
        node = node.parent
    solution.reverse()
    return solution

def genChildren(parent):
    children = []
    nodeState = parent.state

    sepIndex = nodeState.index(sep)

    if(sepIndex + 1 <= len(nodeState) - 1):
        childState = list(nodeState)
        childState[sepIndex], childState[sepIndex + 1] = nodeState[sepIndex + 1], nodeState[sepIndex]
        children.append(Node(childState, parent))
    if(sepIndex - 1 >= 0):
        childState = list(nodeState)
        childState[sepIndex], childState[sepIndex - 1] = nodeState[sepIndex - 1], nodeState[sepIndex]
        children.append(Node(childState, parent))
    if(sepIndex + 2 <= len(childState) - 1):
        childState = list(nodeState)
        childState[sepIndex ], childState[sepIndex + 2] = nodeState[sepIndex + 2], nodeState[sepIndex]
        children.append(Node(childState, parent))
    if(sepIndex - 2 >= 0):
        childState = list(nodeState)
        childState[sepIndex ], childState[sepIndex - 2] = nodeState[sepIndex - 2], nodeState[sepIndex]
        children.append(Node(childState, parent))

    return children

def search(node, goal):

    openedQueue = []
#    openedQueue.append(node)
#    heapq.heappush(openedQueue, node)
    openedHash = {node.id:node}
    closedHash = {}

    while(openedQueue):
        # update the heap
        heapq.heapify(openedQueue)

        # choose the node with the lowest heuristic value as currentNode
        currentNode = heapq.heappop(openedQueue)
        del openedHash[currentNode.id]

        closedHash[currentNode.id] = currentNode

        if(currentNode.state == goal):
            print("done!")
            return currentNode, closedHash, openedHash

        # generate all possible children (ie. possible states of next move)
        genChildren(currentNode)

        for child in currentNode.children:
            if child.id in closedHash:
                child = closedHash[child.id]
            elif child.id in openedHash:
                child = openedHash[child.id]

            # if child got a unique state
            if not child.id in closedHash and child.id not in openedHash:
                # calculate heuristic for child state
                attachAndEval(child, currentNode, goal)
                heapq.heappush(openedQueue, child)
                openedHash[child.id] = child
            elif currentNode.g + 1 < child.g:
                # if child state already generated, see if this one's G-score is better, if yes --> update
                attachAndEval(child, currentNode , goal)
                if child.id in closedHash:
                    propG(child, goal)

def attachAndEval(child, parent, goal):
    child.parent = parent
    child.genHeuristic(goal)
    child.g = parent.g + 1
    child.f = child.g + child.h

def propG(parent, goal):
    for child in parent.children:
        if parent.g + 1 < child.g:
            child.parent = parent
            child.g = parent.g + 1
            child.genHeuristic(goal)
            child.f = child.g + child.h
            propG(child, goal)

def init():
    startTime = time.time()

    checkers = 24
    goal = [x for i in range(checkers / 2)] + [sep] + [ o for j in range(checkers / 2)]

    start = list(goal)
    start.reverse()

    def aStar(start, goal):
        node = Node(start)
        node, opened, closed = search(node, goal)
        solution = solutionSet(node)

        for state in solution:
            print (state, solution.index(state) + 1)

        print ("A* - Solution length: %s - Closed nodes: %s - Opened nodes: %s - Total nodes: %s" % (len(solution), len(closed), len(opened), len(closed) + len(opened)))

    def rundfs(start, goal):
        node = Node(start)
        solutionNode, nodes = dfs(node, goal)
        solution = solutionSet(solutionNode)

        print ("DFS - Solution length: %s - Total nodes: %s" % (len(solution), len(nodes)))

    def runbfs(start, goal):
        node = Node(start)
        solutionNode, nodes = bfs(node, goal)
        solution = solutionSet(solutionNode)

        print ("BFS - Solution length: %s - Total nodes: %s" % (len(solution), len(nodes)))


    aStar(start, goal)

    print (time.time() - startTime) * 1000

    None

init()

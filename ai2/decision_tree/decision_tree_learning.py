from random import  randrange
from collections import deque
from copy import deepcopy
from matplotlib.mlab import log2
from numpy.core.numeric import inf

class Example(object):
    def __init__(self, line):
        # line will be 7 attributes and 1 class
        self.line = line
        self.classification = int(line.split()[-1].strip())
        self.attributeValues = [int(i.strip()) for i in line.split()[0:-1]]
    
    def attributeValue(self, attribute):
        return self.attributeValues[attribute.name-1]

class Node(object):
    def __init__(self, name):
        self.name = name
        self.values = [1, 2]
        self.children = []
        self.parent = None
        self.classification = None
        self.importance = None
    
    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def __str__(self):
        return printNode(self)
    
    def isClassNode(self):
        return not len(self.children);
    
    def choose(self, value):
        if value == 1:
            return self.children[0]
        elif value == 2:
            return self.children[1]

# returns the most common classification classification among a set of examples, breaking ties randomly
def pluralityValue(parent_examples):
    sum = 0.
    for example in parent_examples:
        sum += example.classification

    classification = sum / len(parent_examples)
    if classification == 1.5:
        return randrange(1, 3)
    elif classification < 1.5:
        return 1
    return 2

# getMostImportantNodeFromEntropy based on information gain (highest entropy)
def getMostImportantNodeFromEntropy(attributes, examples):
    def entropy(q):
        return -(q * log2(q) + (1 - q) * log2(1 - q))

    def importanceSingleAttribute(attribute, examples, p, n):
        # worst workaround of the century in order to avoid division by zero
        pk1 = 1e-10
        nk1 = 1e-10
        pk2 = 1e-10
        nk2 = 1e-10
        
        # hard coded arithmatic ftw >___>
        for example in examples:
            if example.attributeValue(attribute) == 2 and example.classification == 2:
                pk1 += 1
            elif example.attributeValue(attribute) == 2 and example.classification == 1:
                nk1 += 1
            elif example.attributeValue(attribute) == 1 and example.classification == 2:
                pk2 += 1
            elif example.attributeValue(attribute) == 1 and example.classification == 1:
                nk2 += 1
        entropy1 = entropy(pk1 / (pk1 + nk1))
        entropy2 = entropy(pk2 / (pk2 + nk2))
        remainder = (pk1 + nk1) / (p + n) * entropy1 + (pk2 + nk2) / (p + n) * entropy2   
#         print remainder, attribute.name
        return remainder 

    # find the amount of positive examples
    p = 0
    for e in examples:
        if e.classification == 2:
            p += 1
    # negative example
    n = len(examples) - p

    # get the entropy for all attributes
    minimum = inf
    for attribute in attributes:
        attribute.importance = importanceSingleAttribute(attribute, examples, p, n)
        if attribute.importance < minimum:
            minimum = attribute.importance
    
    # narrow down the attributes list to only those with the lowest entropy
    mostImportant = []
    for attribute in attributes:
        if attribute.importance == minimum:
            mostImportant.append(attribute)
    
    # return the attribute with the least entropy, randomize ties
    return mostImportant[randrange(0, len(mostImportant))]

# random getMostImportantNodeFromEntropy
def getRandomNode(attributes, examples):
    return attributes[randrange(0, len(attributes))]

# boolean classification: all the examples True or False?
def equalClassifications(examples):
    test = examples[0].classification
    for node in examples:
        if node.classification is not test:
            return False
    return True

def empty(lst):
    return not len(lst)

# the actual decision tree learning algorithm
def decisionTreeLearning(examples, attributes, parent_examples, random):
    if empty(examples):
        child = Node("leaf")
        child.classification = pluralityValue(parent_examples)
        return child
    # if all the remaining examples have the same classification we can surely answer yes or no
    elif equalClassifications(examples):
        child = Node("leaf")
        child.classification = examples[0].classification
        return child
    # if there are no attributes left, but both positive and negative examples, 
    # it means that these examples have exactly the same description but different 
    # classification. Ie. there is noise in the system! 
    elif empty(attributes):
        child = Node("leaf")
        child.classification = pluralityValue(examples)
        return child
    else:
        # find the most important name
        if random:
            mostImportantNode = getRandomNode(attributes, examples)
        else:
            mostImportantNode = getMostImportantNodeFromEntropy(attributes, examples)
        
        # remove the most imporant node from the attribute list
        attributes.remove(mostImportantNode)

        for value in mostImportantNode.values:
            exs = []
            for e in examples:
                if e.attributeValue(mostImportantNode) == value:
                    exs.append(e)
            
            # recursion
            childNode = decisionTreeLearning(exs, deepcopy(attributes) , examples, random)
            
            # add mostImportantNode branch to tree 
            mostImportantNode.addChild(childNode)

        return mostImportantNode 

def initFile(path):
    examples = []
    # or something liek this, not sure lols
    with open(path) as fp:
        for line in fp:
            examples.append(Example(line))
    return examples

def getTraining():
    return initFile('training.txt')
    
def getTest():
    return initFile('test.txt')

def getAttributes():
    return [Node(name) for name in range(len(getTest()[0].attributeValues))]

# print node with with indention based how deep within the tree the node was found
def printNode(node):
    space = ""
    tmpNode = node
    
    # add padding 
    while(tmpNode.parent != None):
        space += "  "
        tmpNode = tmpNode.parent

    if node.isClassNode():
        nodeType = "class " + str(node.classification)
    else:
        nodeType = "attribute " + str(node.name)
    return space + nodeType

# print the entire tree in a semi-pretty fashion
def printTree(root):
    queue = deque()
    queue.append(tree)
    count = 1
    while(queue):
        node = queue.pop()
        print str(count) + "\t" + str(node) 
        count += 1
        for child in node.children:
            queue.append(child)

def classifyTestData(tree, test):
    def classifySingleExample(tree, example):
        node = tree
        while node:
            value = example.attributeValue(node)
            node = node.choose(value)
            if node.isClassNode():
                return node.classification == example.classification

    yes = 0.
    for example in test:
        didItHit = classifySingleExample(tree, example)
#         print str(didItHit) + " " + str(example.line)
        if didItHit:
            yes += 1
    
    print "Hit/miss:" , yes ,"/" ,len(test)
    return yes / len(test)
 
attributes = getAttributes()
training = getTraining()
test = getTest()

sum = 0.
iterations = 1

for i in range(iterations):
    tree = decisionTreeLearning(deepcopy(training), deepcopy(attributes), deepcopy(training), True)
    printTree(tree)
    classify = classifyTestData(tree, test)
    sum += classify
print "Tree converges towards:" ,sum / iterations , "after" ,iterations, "iteration(s)"








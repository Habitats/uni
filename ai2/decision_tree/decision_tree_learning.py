class DecisionTree(object):
    def __init__(self, rootNode):
        self.rootNode = rootNode

class Node(object):
    def __init__(self):
        continue

def initExamples():
    examples = []
    return examples

def initAttributes():
    attributes = []
    return attributes

def pluralityValue(parent_examples):
    continue

def importance(a, examples):
    continue

def equalClassifications(examples):
    test = examples[0].classification
    for e in examples:
        if e.classification is not test:
            return False
    return True

def empty(list):
    return not len(list)


# pseudocode 
def decisionTreeLearning(examples, attributes, parent_examples):
    if empty(examples):
        return pluralityValue(parent_examples)
    elif equalClassifications(examples):
        return examples.classification(); 
    elif empty(attributes):
        return pluralityValue(examples)
    else:
        # find the importance of every attribute 
        importances = [importance(a, examples) for a in attributes];
        
        # find the most imporant attribute
        a = max(importances)

#         tree = new decision tree with root test A
        tree = DecisionTree(a)
        for vk in a:
            exs = []
            for e in examples:
                if e.attribute(a) == vk:
                    exs.append(e)
            
            # remove attribute a from attributes
            attributes.remove(a)
            # recursion
            subtree = decisionTreeLearning(exs, attributes, examples)
            
#             add a branch to tree with label a = vK and subtree subtree
            tree.addBranch(vk, subtree)

        return tree

        
        

# Back-Propagation Neural Networks
# 
# Written in Python.  See http://www.python.org/
# Placed in the public domain.
# Neil Schemenauer <nas@arctrix.com>

import math
import random
import string

random.seed(0)

# calculate a random number where:  a <= rand < b
def rand(a, b):
    return (b-a)*random.random() + a

# Make a matrix (we could use NumPy to speed this up)
def makeMatrix(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill]*J)
    return m

# our logFunc function, tanh is a little nicer than the standard 1/(1+e^-x)
def logFunc(x):
    return math.tanh(x)

# derivative of our logFunc function, in terms of the output (i.e. y)
def logFuncDerivative(y):
    return 1.0 - y**2

class NN:
    def __init__(self, ni, nh, no):
        # number of input, hidden, and output nodes
        self.numInputs = ni + 1 # +1 for bias node
        self.numHidden = nh
        self.numOutputs = no

        # activations for nodes
        self.inputActivation = [1.0]*self.numInputs
        self.hiddenActivations = [1.0]*self.numHidden
        self.outputActivations = [1.0]*self.numOutputs
        
        # create weights
        self.weightsInput = makeMatrix(self.numInputs, self.numHidden)
        self.weigthsOutput = makeMatrix(self.numHidden, self.numOutputs)
        # set them to random vaules
        for i in range(self.numInputs):
            for j in range(self.numHidden):
                self.weightsInput[i][j] = rand(-0.2, 0.2)
        for j in range(self.numHidden):
            for k in range(self.numOutputs):
                self.weigthsOutput[j][k] = rand(-2.0, 2.0)

        # last change in weights for momentum   
        self.ci = makeMatrix(self.numInputs, self.numHidden)
        self.co = makeMatrix(self.numHidden, self.numOutputs)

    def propagate(self, inputs):
        if len(inputs) != self.numInputs-1:
            raise ValueError('wrong number of inputs')

        # input activations
        for i in range(self.numInputs-1):
            #self.inputActivation[i] = logFunc(inputs[i])
            self.inputActivation[i] = inputs[i]

        # hidden activations
        for j in range(self.numHidden):
            sum = 0.0
            for i in range(self.numInputs):
                sum = sum + self.inputActivation[i] * self.weightsInput[i][j]
            self.hiddenActivations[j] = logFunc(sum)

        # output activations
        for k in range(self.numOutputs):
            sum = 0.0
            for j in range(self.numHidden):
                sum = sum + self.hiddenActivations[j] * self.weigthsOutput[j][k]
            self.outputActivations[k] = logFunc(sum)

        return self.outputActivations[:]


    def backPropagate(self, targets, learningRate, M):
        if len(targets) != self.numOutputs:
            raise ValueError('wrong number of target values')

        # calculate error terms for output
        deltaOutput = [0.0] * self.numOutputs
        for k in range(self.numOutputs):
            error = targets[k]-self.outputActivations[k]
            deltaOutput[k] = logFuncDerivative(self.outputActivations[k]) * error

        # calculate error terms for hidden
        deltaHidden = [0.0] * self.numHidden
        for j in range(self.numHidden):
            error = 0.0
            for k in range(self.numOutputs):
                error = error + deltaOutput[k]*self.weigthsOutput[j][k]
            deltaHidden[j] = logFuncDerivative(self.hiddenActivations[j]) * error

        # propagate output weights
        for j in range(self.numHidden):
            for k in range(self.numOutputs):
                change = deltaOutput[k]*self.hiddenActivations[j]
                self.weigthsOutput[j][k] = self.weigthsOutput[j][k] + learningRate*change + M*self.co[j][k]
                self.co[j][k] = change
                #print learningRate*change, M*self.co[j][k]

        # propagate input weights
        for i in range(self.numInputs):
            for j in range(self.numHidden):
                change = deltaHidden[j]*self.inputActivation[i]
                self.weightsInput[i][j] = self.weightsInput[i][j] + learningRate*change + M*self.ci[i][j]
                self.ci[i][j] = change

        # calculate error
        error = 0.0
        for k in range(len(targets)):
            error = error + 0.5*(targets[k]-self.outputActivations[k])**2
        return error


    def test(self, patterns):
        for p in patterns:
            print(p[0], '->', self.propagate(p[0]))

    def weights(self):
        print('Input weights:')
        for i in range(self.numInputs):
            print(self.weightsInput[i])
        print()
        print('Output weights:')
        for j in range(self.numHidden):
            print(self.weigthsOutput[j])

    def train(self, patterns, iterations=1000, N=0.5, M=0.1):
        # N: learning rate
        # M: momentum factor
        for i in range(iterations):
            error = 0.0
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.propagate(inputs)
                error = error + self.backPropagate(targets, N, M)
            if i % 100 == 0:
                print('error %-.5f' % error)


def demo():
    # Teach network XOR function
    pat = [
        [[0,0], [0]],
        [[0,1], [1]],
        [[1,0], [1]],
        [[1,1], [0]]
    ]

    # create a network with two input, two hidden, and one output nodes
    n = NN(2, 2, 1)
    # train it with some patterns
    n.train(pat)
    # test it
    n.test(pat)



if __name__ == '__main__':
    demo()
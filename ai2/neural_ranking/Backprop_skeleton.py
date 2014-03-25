import math
import random
import copy

# The transfer function of neurons, g(x)
def logFunc(x):
    return (1.0 / (1.0 + math.exp(-x)))

# The derivative of the transfer function, g'(x)
def logFuncDerivative(x):
    return math.exp(-x) / (pow(math.exp(-x) + 1, 2))

def randomFloat(low, high):
    return random.random() * (high - low) + low

# Initializes a matrix of all zeros
def makeMatrix(I, J):
    m = []
    for i in range(I):
        m.append([0] * J)
    return m

class NN:  # Neural Network
    def __init__(self, numInputs, numHidden, learningRate=0.001):
        # Inputs: number of input and hidden nodes. Assuming a single output node.
        # +1 for bias node: A node with a constant input of 1. Used to shift the transfer function.
        self.numInputs = numInputs + 1
        self.numHidden = numHidden

        # Current activation levels for nodes (in other words, the nodes' output value)
        self.inputActivation = [1.0] * self.numInputs
        self.hiddenActivations = [1.0] * self.numHidden
        self.outputActivation = 1.0  # Assuming a single output.
        self.learningRate = learningRate

        # create weights
        # A matrix with all weights from input layer to hidden layer
        self.weightsInput = makeMatrix(self.numInputs, self.numHidden)
        # A list with all weights from hidden layer to the single output neuron.
        self.weightsOutput = [0 for i in range(self.numHidden)]  # Assuming single output
        # set them to random vaules
        for i in range(self.numInputs):
            for j in range(self.numHidden):
                self.weightsInput[i][j] = randomFloat(-0.5, 0.5)
        for j in range(self.numHidden):
            self.weightsOutput[j] = randomFloat(-0.5, 0.5)

        # Data for the backpropagation step in RankNets.
        # For storing the previous activation levels (output levels) of all neurons
        self.prevInputActivations = []
        self.prevHiddenActivations = []
        self.prevOutputActivation = 0
        # For storing the previous delta in the output and hidden layer
        self.prevDeltaOutput = 0
        self.prevDeltaHidden = [0 for i in range(self.numHidden)]
        # For storing the current delta in the same layers
        self.deltaOutput = 0
        self.deltaHidden = [0 for i in range(self.numHidden)]

    def propagate(self, inputs):
        if len(inputs) != self.numInputs - 1:
            raise ValueError('wrong number of inputs')
        # input activations
        self.prevInputActivations = copy.deepcopy(self.inputActivation)
        for i in range(self.numInputs - 1):
            self.inputActivation[i] = inputs[i]
        self.inputActivation[-1] = 1  # Set bias node to -1.
        # hidden activations
        self.prevHiddenActivations = copy.deepcopy(self.hiddenActivations)
        for j in range(self.numHidden):
            sum = 0.0
            for i in range(self.numInputs):
                sum = sum + self.inputActivation[i] * self.weightsInput[i][j]
            self.hiddenActivations[j] = logFunc(sum)
        # output activations
        self.prevOutputActivation = self.outputActivation
        sum = 0.0
        for j in range(self.numHidden):
            sum = sum + self.hiddenActivations[j] * self.weightsOutput[j]
        self.outputActivation = logFunc(sum)
        return self.outputActivation

    def computeOutputDelta(self):
        oa = self.prevOutputActivation
        ob = self.outputActivation
        # equation 1
        pab = logFunc(oa - ob)
        # equation 2
        doa = logFuncDerivative(oa) * (1 - pab)
        # equation 3
        dob = logFuncDerivative(ob) * (1 - pab)
        
        self.deltaOutput = dob
        self.prevDeltaOutput = doa

    def computeHiddenDelta(self):
        delta = self.prevDeltaOutput - self.deltaOutput
        for i in range(self.numHidden):
            # equation 4
            self.prevDeltaHidden[i] = logFuncDerivative(self.prevHiddenActivations[i]) * self.deltaOutput * delta
            # equation 5
            self.deltaHidden[i] = logFuncDerivative(self.hiddenActivations[i]) * self.deltaOutput * delta

    def updateWeights(self):
        # update output weights
        for i in range(self.numHidden):
            change_a = self.prevDeltaOutput* self.prevHiddenActivations[i]
            change_b = self.deltaOutput * self.hiddenActivations[i]
            self.weightsOutput[i] = self.weightsOutput[i] + self.learningRate * (change_a - change_b)
        
        # update input weights
        for i in range(self.numInputs):
            for j in range(self.numHidden):
                change = self.deltaHidden[j] * self.inputActivation[i]
                self.weightsInput[i][j] = self.weightsInput[i][j] + self.learningRate * change

    def backpropagate(self):
        # Forward propagation of a training pattern's input through the neural network in 
        # order to generate the propagation's output activations.
        self.computeOutputDelta()
        # Backward propagation of the propagation's output activations through the neural network 
        # using the training pattern target in order to generate the deltas of all output and hidden neurons.
        self.computeHiddenDelta()
        self.updateWeights()

    # Prints the network weights
    def weights(self):
        print('Input weights:')
        for i in range(self.numInputs):
            print(self.weightsInput[i])
        print()
        print('Output weights:')
        print(self.weightsOutput)

    def train(self, patterns, iterations=1):
        for i in range(iterations):
            for p in patterns:
                a = p[0].features
                b = p[1].features
                af = self.propagate(a)
                bf = self.propagate(b)
                self.backpropagate()

    def countMisorderedPairs(self, patterns):
        numRight = 0.
        numMiss = 0.
        for p in patterns:
            a = p[0].features
            b = p[1].features
            af = self.propagate(a)
            bf = self.propagate(b)
            if af > bf and p[0].rating > p[1].rating:
                numRight += 1
            else:
                numMiss += 1
        errorRate = numMiss / (numRight + numMiss)
#         print "Num right:" , numRight, "- Num miss:", numMiss, "- Error rate:", errorRate
        print numRight, numMiss, errorRate
        return numRight,numMiss,errorRate

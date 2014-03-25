import Backprop_skeleton as Bp


# Class for holding your data - one object for each line in the dataset
class dataInstance:

    def __init__(self, qid, rating, features):
        self.qid = qid  # ID of the query
        self.rating = rating  # Rating of this site for this query
        self.features = features  # The features of this query-site pair.

    def __str__(self):
        return "Datainstance - qid: " + str(self.qid) + ". rating: " + str(self.rating) + ". features: " + str(self.features)

# A class that holds all the data in one of our sets (the training set or the testset)
class dataHolder:

    def __init__(self, dataset):
        self.dataset = self.loadData(dataset)

    def loadData(self, file):
        # Input: A file with the data.
        # Output: A dict mapping each query ID to the relevant documents, like this: dataset[queryID] = [dataInstance1, dataInstance2, ...]
        data = open(file)
        dataset = {}
        for line in data:
            # Extracting all the useful info from the line of data
            lineData = line.split()
            rating = int(lineData[0])
            qid = int(lineData[1].split(':')[1])
            features = []
            for elem in lineData[2:]:
                if '#docid' in elem:  # We reached a comment. Line done.
                    break
                features.append(float(elem.split(':')[1]))
            # Creating a new data instance, inserting in the dict.
            di = dataInstance(qid, rating, features)
            if qid in dataset.keys():
                dataset[qid].append(di)
            else:
                dataset[qid] = [di]
        return dataset


def runRanker(trainingset, testset):
    # Dataholders for training and testset
    dhTraining = dataHolder(trainingset)
    dhTesting = dataHolder(testset)

    # Creating an ANN instance - feel free to experiment with the learning rate (the third parameter).
    nn = Bp.NN(46, 10, 0.001)

    pairs = set()
    def genPairs(instanceData):
        for qid in dhTraining.dataset.keys():
            # This iterates through every query ID in our training set
            instanceData = dhTraining.dataset[qid]  # All data instanceData (query, features, rating) for query qid
            rank0 = filter(lambda x: x.rating == 0, instanceData)
            rank1 = filter(lambda x: x.rating == 1, instanceData)
            rank2 = filter(lambda x: x.rating == 2, instanceData)
            pairs.update((docHigher, docLower) for docHigher in rank2 for docLower in rank1)
            pairs.update((docHigher, docLower) for docHigher in rank2 for docLower in rank0)
            pairs.update((docHigher, docLower) for docHigher in rank1 for docLower in rank0)
    
        return list(pairs)

    trainingPatterns = genPairs(dhTraining)
    testPatterns = genPairs(dhTesting)

    # Check ANN performance before training
    nn.countMisorderedPairs(testPatterns)
    misorderedPairsTraining = []
    plots = []
    for i in range(25):
        nn.train(trainingPatterns, iterations=1)
        hitInfo = nn.countMisorderedPairs(testPatterns)
        misorderedPairsTraining.append(hitInfo)

    return misorderedPairsTraining


errorRates = []
for i in range(5):
    misorderedPairsTraining = runRanker("train.txt", "test.txt")
    print "#"


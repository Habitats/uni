import matplotlib.pyplot as plt
import copy

with open("plot.txt") as f:
    i = 0
    a = []
    plt.axis([0, 25, 0, 1])
    all = []
    for line in f:
        if "#" in line:
#             plt.plot(*zip(*a))
            all.append(copy.deepcopy(a))
            i = 0
            a = []
        else:
            a.append([i, line.split()[-1]])
            i += 1
            print line
    
    # initialize the average graph
    avg = [[0 for i in range(len(all[0][0]))] for j in range(len(all[0])-1)]
    for i in range(len(avg)):
        avg[i][0] = i
    
    # iterate over x, y pairs
    for i in range(len(all[0])-1):
        # iterate over the different results
        for k in range(len(all)):
#             print all[k][i]
#             print avg[i]
            avg[i][1] += float(all[k][i][1])
        avg[i][1] /= len(all)
#         print i
        print avg[i][0], avg[i][1]

    plt.plot(*zip(*avg))






plt.show()

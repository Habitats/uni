import matplotlib.pyplot as plt

with open("plot.txt") as f:
    i = 0
    a = []
    plt.axis([0, 25, 0, 1])
    for line in f:
        if "#" in line:
            plt.plot(*zip(*a))
            i = 0
            a = []
        else:
            a.append([i, line.split()[-1]])
            i += 1
            print line


plt.show()

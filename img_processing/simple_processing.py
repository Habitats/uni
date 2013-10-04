import numpy as np
import pylab as pyl
import matplotlib.pyplot as plt

# read
I = pyl.imread("test.png")

nx = I.shape[0]
ny = I.shape[1]

imggray = np.zeros((nx, ny), dtype = np.double)
imggray[1:nx, 1:ny] = I[1:nx, 1:ny, 1]

tmp = 255 * np.ones((nx, ny), dtype = np.double)

# process
myout = tmp - imggray

plt.imshow(myout, origin = 'upper', cmap = plt.cm.gray)
interpolation = "nearest"

plt.show()
# plt.savefig("output.png")
